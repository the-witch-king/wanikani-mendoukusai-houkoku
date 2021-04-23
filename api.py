import requests
import sys

class WaniKaniApi:
    def __init__(self, api_key: str):
        self.headers = { "Authorization": "Bearer " + api_key }

    # Not used...yet
    def get_user_level(self):
        response_json = requests.get("https://api.wanikani.com/v2/user", headers = self.headers).json()
        level = response_json["data"]["level"]
        return level

    # Get all user's assignments
    def get_all_assignments(self, url = "https://api.wanikani.com/v2/assignments", assignments = []):
        params = { "burned": "false", "started": "true"}
        response_json = requests.get(url, params = params, headers = self.headers).json()
        items = assignments + response_json["data"]
        next_url = response_json["pages"]["next_url"]

        percent = (len(assignments) / int(response_json["total_count"])) * 100
        sys.stdout.flush()
        sys.stdout.write("Loading Assignments [%.2f%%]\r" % (percent))
        sys.stdout.flush()

        if next_url == None:
            return items

        return self.get_all_assignments(next_url, items)

    # Get all user's subjects
    def get_all_subjects(self, ids = "", url = "https://api.wanikani.com/v2/subjects", subjects = []):
        params = { "ids": ids }
        response_json = requests.get(url, params = params, headers = self.headers).json()
        items = subjects + response_json["data"]
        next_url = response_json["pages"]["next_url"]

        percent = (len(subjects) / int(response_json["total_count"])) * 100
        sys.stdout.flush()
        sys.stdout.write("Loading Subjects [%.2f%%]\r" % (percent))
        sys.stdout.flush()

        if next_url == None:
            return items

        return self.get_all_subjects(ids, next_url, items)

