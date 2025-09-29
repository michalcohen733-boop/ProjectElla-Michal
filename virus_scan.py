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
