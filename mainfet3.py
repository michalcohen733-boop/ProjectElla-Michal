from virus_scan import VirusScan

if __name__ == "__main__":
    API_KEY = "4da69d055a6ed3dc5a364df98ec8e6ec92fb935bda1b63c852a99b5ee2da4b8f"
    scanner = VirusScan(API_KEY)
    file_hash = "420e57b017066b44e05ea1577f6e2e12"
    stats = scanner.get_virustotal_score(file_hash)
    print(stats)
