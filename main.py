import requests

class VirusScan:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://www.virustotal.com/api/v3/files/"

    def get_virusTotal_score(self, file_hash):
        url = f"{self.base_url}{file_hash}"
        headers = {
            "accept": "application/json",
            "x-apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
        return None


if __name__ == "__main__":
    API_KEY = "4da69d055a6ed3dc5a364df98ec8e6ec92fb935bda1b63c852a99b5ee2da4b8f"
    scanner = VirusScan(API_KEY)
    file_hash = "420e57b017066b44e05ea1577f6e2e12"
    stats = scanner.get_virusTotal_score(file_hash)
    print(stats)
