from virus_scan import VirusScan
from encoder import *

def go_to_virus_scan(file_hash):
    API_KEY = "4da69d055a6ed3dc5a364df98ec8e6ec92fb935bda1b63c852a99b5ee2da4b8f"
    scanner = VirusScan(API_KEY)
    stats = scanner.get_virustotal_score(file_hash)
    print(stats)
