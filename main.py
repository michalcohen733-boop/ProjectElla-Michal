import os
from importlib.metadata import files

class FileScanner:
    def __init__(self, path):
        self.path = path
        self.files = []

    def get_file_list(self):
        self.files = []
        for root, d_names, f_names in os.walk(self.path):
            for f in f_names:
                if f.endswith('.exe') or f.endswith('.dll'):
                    self.files.append(os.path.join(root, f))
        print(self.files)


def file_read():
    path = input("Enter the file path: ")
    file_scanner = FileScanner(path)
    file_scanner.get_file_list()
    print(file_scanner.files)

def main():
    file_read()

if __name__ == '__main__':
    main()