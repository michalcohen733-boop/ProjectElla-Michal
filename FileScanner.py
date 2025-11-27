from encoder import *
from filelist import *
import os
import sys
from virus_scan import VirusScan
from gotovirustotal import go_to_virus_scan
import time

def get_file_content(file_path):
    file = open(file_path, "rb")
    read_file = file.read()
    #print(read_file)
    return read_file


def get_file_hash(file_path, hash_type = "sha256"):
    if hash_type.lower() == "md5":
        encoder = MD5HASH()
    elif hash_type.lower() == "sha1":
        encoder = SHA1HASH()
    elif hash_type.lower() == "sha256":
        encoder = SHA256HASH()
    else:
        raise ValueError("Invalid hash type")
    encoded = encoder.calculate_hash_value(get_file_content(file_path))
    return encoded


# def print_files_hashes(path):
#     files = FileScanner(path)
#     good_files = files.get_file_list()
#     for file in good_files:
#         hash1 = get_file_hash(file)
#         print(hash1, os.path.basename(file))

def start_scan(path):
    scan = FileScanner(path)
    list_of_files = scan.get_file_list()
    for f in list_of_files:
        file = f
        content= get_file_content(file)
        try:
            hash_value = get_file_hash(file)
            final_result = go_to_virus_scan(hash_value)
            print(final_result)
        except Exception as e:
            print(e)



def main():
    minutes = 300
    path = input("Enter the folder path: ")
    while True:
        start_scan(path)
        time.sleep(minutes)


if __name__ == '__main__':
    main()

