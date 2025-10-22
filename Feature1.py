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
                    #print(f)
                    self.files.append(os.path.join(root, f))
        return self.files




# def check():
#     path = r'C:\Users\Cyber_Mamriot\Desktop\mamriot26\LOL'
#     check = FileScanner(path)
#     print(check.get_file_list())
#
# check() ['C:\\Users\\Cyber_Mamriot\\Desktop\\mamriot26\\LOL\\UnRAR.exe']
#

