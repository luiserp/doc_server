import os
import socket
from socketserver import BaseRequestHandler
import sys
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Callable, List, Tuple
import contextlib

from doc_server.utils.logger import Logger

class Manager:

    def __init__(self, doc_dir, start_port = 8000) -> None:
        self.doc_dir: Path = doc_dir
        self.start_port = start_port
        self.doc_list = list(self.doc_dir.iterdir())
        self.servers: List[Server] = []

    def run_all_servers(self):
        if (len(self.doc_list) == 0):
            Logger.no_docs_to_serve()
            sys.exit()

        Logger.serving_docs(self.doc_dir.absolute())
        for dir in self.doc_list:
            s = self.create_server(str(dir), self.start_port)
            self.start_port = s.port + 1
            self.servers.append(s)
            th = threading.Thread(target=s.start)
            th.start()

    def stop_all_servers(self):
        for s in self.servers:
            s.stop()

    def create_server(self, dir, port):
        try:
            return Server(dir, port)
        except OSError:
            return self.create_server(dir, port + 1)


class Server:

    def __init__(self, dir, port) -> None:
        self.dir = dir
        if(sys.platform.startswith('win32')):
            self.name = str(dir).split('\\')[-1]
        elif(sys.platform.startswith('linux')):
            self.name = str(dir).split('/')[-1]
        else:
            self.name = dir
        self.port = port
        self.httpd = DualStackServer(("", self.port), RequestHandler, directory=self.dir)

    def start(self):
        try:
            Logger.server_on(self.name, self.port)
            self.httpd.serve_forever()    
        except KeyboardInterrupt:
            Logger.keyboard_interrupt()
            sys.exit(0)

    def stop(self):
        self.httpd.shutdown()
        Logger.server_of(self.name)

class RequestHandler(SimpleHTTPRequestHandler):

    def log_request(self, code: int or str = ..., size: int or str = ...) -> None:
        return ""

    def log_error(self, format: str, *args: Any) -> None:
        return ""

    def log_message(self, format: str, *args: Any) -> None:
        return ""

# ensure dual-stack is not disabled; ref #38907
class DualStackServer(ThreadingHTTPServer):
    
    def __init__(self, server_address: Tuple[str, int], RequestHandlerClass: Callable[..., BaseRequestHandler], bind_and_activate: bool = ..., directory = os.getcwd()) -> None:
        super().__init__(server_address, RequestHandlerClass, bind_and_activate)
        self.directory = directory

    def server_bind(self):
        # suppress exception when protocol is IPv4
        with contextlib.suppress(Exception):
            self.socket.setsockopt(
                socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        return super().server_bind()

    def finish_request(self, request, client_address):
        self.RequestHandlerClass(request, client_address, self,
                                    directory=self.directory)
