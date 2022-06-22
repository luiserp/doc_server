class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Logger:
    
    @staticmethod
    def serving_docs(doc_dir):
        print(f"{bcolors.HEADER}Documentation directory: {bcolors.ENDC}{bcolors.OKBLUE}{doc_dir}{bcolors.ENDC}")

    @staticmethod
    def server_on(name, port):
        print(f"{bcolors.OKGREEN}{name}{bcolors.ENDC} on {bcolors.OKCYAN}{bcolors.UNDERLINE} http://localhost:{port}{bcolors.ENDC}{bcolors.ENDC}")

    @staticmethod
    def server_of(name):
        print(f"{bcolors.WARNING}{name} {bcolors.ENDC}{bcolors.FAIL}down{bcolors.ENDC}")

    @staticmethod
    def keyboard_interrupt():
        print(f"{bcolors.FAIL}\nKeyboard interrupt received, exiting.{bcolors.ENDC}")

    @staticmethod
    def exit_clue():
        print(f"{bcolors.WARNING}\"quit\" or \"q\" to exit{bcolors.ENDC}")

    @staticmethod
    def no_docs_to_serve():
        print(f"{bcolors.FAIL}There is no docs to serve. Try doc_server [-a | --add_doc] path_to_zip_file{bcolors.ENDC}")

    @staticmethod
    def zip_exctracted(name):
        print(f"The zip file {bcolors.OKCYAN}{name}{bcolors.ENDC} was {bcolors.OKGREEN}successfully added{bcolors.ENDC} to the docs folder")

    @staticmethod
    def not_a_zip(name):
        print(f"{bcolors.FAIL}The file {name} is not a zip file or a zip containing folder.{bcolors.ENDC}")

    @staticmethod
    def no_a_zip_in_this_folder(name):
        print(f"{bcolors.FAIL}There is no one zip in the {bcolors.WARNING}{name}{bcolors.FAIL} folder.{bcolors.ENDC}")
