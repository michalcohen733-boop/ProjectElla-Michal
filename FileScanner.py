from encoder import Encoder
from Feature1 import *
import os
import sys
from virus_scan import VirusScan
from mainfet3 import go_to_virus_scan

def get_file_content(file_path):
    file = open(file_path, "rb")
    read_file = file.read()
    #print(read_file)
    return read_file


def get_file_hash(file_path):
    encoder = Encoder()
    encoded = encoder.calculate_hash_value(get_file_content(file_path))
    return encoded


# def print_files_hashes(path):
#     files = FileScanner(path)
#     good_files = files.get_file_list()
#     for file in good_files:
#         hash1 = get_file_hash(file)
#         print(hash1, os.path.basename(file))


def main():
    path = input("Enter the folder path: ")
    SCAN = FileScanner(path)
    list_of_files = SCAN.get_file_list()
    for f in list_of_files:
        file = f
        content= get_file_content(file)
        hash_value = get_file_hash(file)
        final_result = go_to_virus_scan(hash_value)
        print(final_result)


if __name__ == '__main__':
    main()

