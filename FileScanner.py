from encoder import Encoder
from Feature1 import *


def get_file_content(file_path):
    file = open(file_path, "rb")
    read_file = file.read()
    return read_file


def get_file_hash(file_path):
    encoder = Encoder()
    encoded = encoder.calculate_hash_value(get_file_content(file_path))
    return encoded


def print_files_hashes(path):
    files = FileScanner(path)
    good_files = files.get_file_list()
    for file in good_files:
        hash1 = get_file_hash(file)
        print(hash1, os.path.basename(file))


def main():
    path = input("Enter the file path: ")
    print_files_hashes(path)


if __name__ == '__main__':
    main()

