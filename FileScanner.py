from encoder import *
from filelist import *
import datetime
import os
import sys
from virus_scan import VirusScan
from gotovirustotal import go_to_virus_scan
import time
from pathlib import Path
import shutil

QUARANTINE_FOLDER = Path(r"C:\quarantine")


def create_quarantine():
    try:
        QUARANTINE_FOLDER.mkdir(exist_ok=True)
        print(f"Folder '{QUARANTINE_FOLDER}' is ready.")
    except Exception as e:
        print(f"Error creating quarantine folder: {e}")


def add_to_quarantine(filename):
    filename = Path(filename)  # convert to Path object if it's a string
    if not filename.exists() or not filename.is_file():
        print(f"File '{filename}' does not exist.")
        return None

    QUARANTINE_FOLDER.mkdir(exist_ok=True)

    dest_path = QUARANTINE_FOLDER / filename.name

    try:
        shutil.move(str(filename), str(dest_path))
        print(f"Added to quarantine: {filename.name}")
    except Exception as e:
        print(f"Failed to quarantine {filename.name}: {e}")
        return None


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

def terminate_file(file_path):
    file_path = Path(file_path)

    if not file_path.exists() or not file_path.is_file():
        print(f"File '{file_path}' does not exist.")
        return

    if file_path.suffix.lower() == ".dll":
        new_suffix = ".exe"
    elif file_path.suffix.lower() == ".exe":
        new_suffix = ".dll"
    else:
        print(f"File '{file_path.name}' has unsupported extension. Skipping.")
        return

    new_file_path = file_path.with_suffix(new_suffix)

    try:
        file_path.rename(new_file_path)
        print(f"Terminated file: {file_path.name} → {new_file_path.name}")
    except Exception as e:
        print(f"Failed to terminate {file_path.name}: {e}")

# def print_files_hashes(path):
#     files = FileScanner(path)
#     good_files = files.get_file_list()
#     for file in good_files:
#         hash1 = get_file_hash(file)
#         print(hash1, os.path.basename(file))

def start_scan(path):

    create_quarantine()
    f = open("report.txt", "a")
    scan = FileScanner(path)
    list_of_files = scan.get_file_list()
    for i in list_of_files:
        f.write(i + ", ")
        x = datetime.datetime.now()
        f.write(str(x) + ", ")
        file = i
        #print("this is file" + file)
        content = get_file_content(file)
        try:
            hash_value = get_file_hash(file)
            final_result = go_to_virus_scan(hash_value)
            print(final_result)
            if final_result == None:
                f.write("file is good" + "\n")
            else:
                quarantined_file = add_to_quarantine(file)
                if quarantined_file:
                    terminate_file(quarantined_file)
                f.write(str(final_result) + "\n")
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

