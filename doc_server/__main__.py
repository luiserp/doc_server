from argparse import ArgumentParser
from pathlib import Path
import sys
import webbrowser
from zipfile import ZipFile, is_zipfile
from doc_server.utils.logger import Logger
from doc_server.utils.server import Manager, DualStackServer

def main():
    parser = ArgumentParser(description="Manage and review documentations of some languages and technologies")
    parser.add_argument('-d', '--directory', default=str(Path().home().joinpath('.doc_server_docs')), help='The directory where the documentation is stored')
    parser.add_argument('-a', '--add_doc', help='The route of the zip file containing the doc')
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

def exctract_zip(zip, path):
     with ZipFile(zip) as zip:
            zip.extractall(path)
            Logger.zip_exctracted(zip.filename)

if __name__ == "__main__":
    main()


# Open the web browser
# webbrowser.open('http://localhost:{}'.format(port))