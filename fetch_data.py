"""
Fetch data from Procore API or use demo data
"""

import requests

# Try to import config, fall back to demo mode if not found
try:
    from config import (
        PROCORE_CLIENT_ID,
        PROCORE_CLIENT_SECRET,
        PROCORE_API_BASE,
        COMPANY_ID,
        PROJECT_ID
    )
    DEMO_MODE = False
except ImportError:
    DEMO_MODE = True
    print("No config.py found - running in DEMO MODE with sample data")

from sample_data import SAMPLE_RFIS, SAMPLE_SUBMITTALS, SAMPLE_DAILY_LOGS


class ProcoreClient:
    def __init__(self, demo_mode=None):
        if demo_mode is not None:
            self.demo_mode = demo_mode
        else:
            self.demo_mode = DEMO_MODE

        if not self.demo_mode:
            self.base_url = PROCORE_API_BASE
            self.access_token = None

    def authenticate(self):
        """Get access token from Procore OAuth"""
        if self.demo_mode:
            print("Demo mode - no authentication needed")
            return True

        # Real OAuth flow would go here
        print("Authentication required - see Procore Developer Portal")
        return False

    def get_rfis(self):
        """Fetch all RFIs for the project"""
        if self.demo_mode:
            return SAMPLE_RFIS

        endpoint = f"{self.base_url}/projects/{PROJECT_ID}/rfis"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Procore-Company-Id": COMPANY_ID
        }
        response = requests.get(endpoint, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching RFIs: {response.status_code}")
            return []

    def get_submittals(self):
        """Fetch all submittals for the project"""
        if self.demo_mode:
            return SAMPLE_SUBMITTALS

        endpoint = f"{self.base_url}/projects/{PROJECT_ID}/submittals"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Procore-Company-Id": COMPANY_ID
        }
        response = requests.get(endpoint, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching submittals: {response.status_code}")
            return []

    def get_daily_logs(self):
        """Fetch daily logs"""
        if self.demo_mode:
            return SAMPLE_DAILY_LOGS

        endpoint = f"{self.base_url}/projects/{PROJECT_ID}/daily_logs"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Procore-Company-Id": COMPANY_ID
        }
        response = requests.get(endpoint, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching daily logs: {response.status_code}")
            return []


if __name__ == "__main__":
    client = ProcoreClient()
    client.authenticate()

    print("\nFetching RFIs...")
    rfis = client.get_rfis()
    print(f"Found {len(rfis)} RFIs")

    print("\nFetching Submittals...")
    submittals = client.get_submittals()
    print(f"Found {len(submittals)} submittals")

    print("\nFetching Daily Logs...")
    logs = client.get_daily_logs()
    print(f"Found {len(logs)} daily logs")
