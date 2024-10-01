import requests
import json
from datetime import datetime, timedelta
import time
from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes
import subprocess
import os

class BPHTracker:
    def __init__(self, api_key):
        self.otx = OTXv2(api_key)
        self.known_infrastructure = {}
        self.changes = []

    def fetch_infrastructure_data(self):
        try:
            infrastructure_data = []
            modified_since = datetime.now() - timedelta(hours=1)
            pulses = self.otx.getsince(modified_since)
            
            for pulse in pulses:
                for indicator in pulse['indicators']:
                    if indicator['type'] in [IndicatorTypes.IPv4, IndicatorTypes.DOMAIN, IndicatorTypes.HOSTNAME]:
                        infrastructure_data.append({
                            'id': indicator['indicator'],
                            'type': indicator['type'],
                            'pulse_name': pulse['name'],
                            'pulse_description': pulse['description'],
                            'created': indicator['created']
                        })
            
            return infrastructure_data
        except Exception as e:
            print(f"Error fetching data: {str(e)}")
            return None

    def compare_and_update(self, new_data):
        changes = []
        for item in new_data:
            item_id = item['id']
            if item_id in self.known_infrastructure:
                if item != self.known_infrastructure[item_id]:
                    changes.append({
                        "type": "updated",
                        "id": item_id,
                        "old": self.known_infrastructure[item_id],
                        "new": item
                    })
            else:
                changes.append({
                    "type": "new",
                    "id": item_id,
                    "data": item
                })
            self.known_infrastructure[item_id] = item
        
        return changes

    def log_changes(self, changes):
        timestamp = datetime.now().isoformat()
        for change in changes:
            change['timestamp'] = timestamp
            self.changes.append(change)
        
        self.changes = self.changes[-100:]  # Keep only the latest 100 changes
        
        try:
            with open("data.json", "w") as json_file:
                json.dump(self.changes, json_file, indent=2)
        except Exception as e:
            print(f"Error writing to data.json: {str(e)}")

    def sync_to_gcs(self):
        bucket_name = "YOUR_BUCKET_NAME"  # Replace with your actual bucket name
        try:
            subprocess.run(["gsutil", "cp", "data.json", f"gs://{bucket_name}/"], check=True)
            print("Successfully synced data.json to GCS")
        except subprocess.CalledProcessError as e:
            print(f"Error syncing to GCS: {str(e)}")

    def run(self, interval=3600):
        while True:
            print("Fetching infrastructure data...")
            new_data = self.fetch_infrastructure_data()
            if new_data:
                changes = self.compare_and_update(new_data)
                if changes:
                    print(f"Detected {len(changes)} changes.")
                    self.log_changes(changes)
                    self.sync_to_gcs()
                else:
                    print("No changes detected.")
            time.sleep(interval)

if __name__ == "__main__":
    api_key = "YOUR_OTX_API_KEY"  # Replace with your actual OTX API key
    tracker = BPHTracker(api_key)
    tracker.run()