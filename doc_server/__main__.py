from argparse import ArgumentParser
from pathlib import Path
from shutil import rmtree
import sys
import webbrowser
from xmlrpc.client import boolean
from zipfile import ZipFile, is_zipfile
from doc_server.utils.logger import Logger
from doc_server.utils.server import Manager, DualStackServer

def main():
    parser = ArgumentParser(description="Manage and review documentations of some languages and technologies")
    parser.add_argument('-d', '--directory', default=str(Path().home().joinpath('.doc_server_docs')), help='The directory where the documentation is stored')
    parser.add_argument('-a', '--add_doc', help='The route of the zip file containing the doc')
    parser.add_argument('-r', '--remove', help='Remove a doc from the list of docs')
    parser.add_argument('-l', '--list',  action="store_true", help='List the available docs')
    args = parser.parse_args()

    path = Path(args.directory)
    if(not path.exists()):
        path.mkdir(exist_ok=True)

    if(args.add_doc):
        z = Path(args.add_doc)
        if(is_zipfile(z)):
            exctract_zip(z, path)

        elif z.is_dir():
            zips = [file for file in z.iterdir() if is_zipfile(file)]
            if(len(zips) == 0):
                Logger.no_a_zip_in_this_folder(z)
            for zip in zips:
                exctract_zip(zip, path)

        else:
            Logger.not_a_zip(args.add_doc)
    elif(args.list):
        Logger.serving_docs(path)
        for dir in path.iterdir():
            Logger.show_dir_name(dir)
    elif(args.remove):
        to_remove = Path(path.joinpath(args.remove))
        if to_remove.exists():
            rmtree(to_remove)
            Logger.directory_deleted(to_remove)
        else:
            Logger.directory_not_found(to_remove)
    else:
        m = Manager(path)
        m.run_all_servers()

        try:
            Logger.exit_clue()
            while input('>> ') not in ['quit', 'q']:
                pass
        except KeyboardInterrupt:
            Logger.keyboard_interrupt()
            
        finally:
            m.stop_all_servers()
            sys.exit(0)

def exctract_zip(zip: Path, path: Path):
    with ZipFile(zip) as zip_file:
        zip_file.extractall(path)

        # if len(zip_file.namelist()) <= 1:
        #     zip_file.extractall(path)
        # else:
        #     zip_file.extractall(path.joinpath(zip.name.split('.')[0]))
        Logger.zip_exctracted(zip_file.filename)

if __name__ == "__main__":
    main()


# Open the web browser
# webbrowser.open('http://localhost:{}'.format(port))