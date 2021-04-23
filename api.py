import requests
import sys

# Not used...yet
def get_user_level(api_key):
    headers = { "Authorization": "Bearer " + api_key }
    response_json = requests.get("https://api.wanikani.com/v2/user", headers = headers).json()
    level = response_json["data"]["level"]
    return level

def get_all_assignments(api_key, url = "https://api.wanikani.com/v2/assignments", assignments = []):
    headers = { "Authorization": "Bearer " + api_key}
    params = { "burned": "false", "started": "true"}
    response_json = requests.get(url, params = params, headers = headers).json()
    items = assignments + response_json["data"]
    next_url = response_json["pages"]["next_url"]

    percent = (len(assignments) / int(response_json["total_count"])) * 100
    sys.stdout.write("Loading Assignments [%.2f%%]\r" % (percent))
    sys.stdout.flush()

    if next_url == None:
        return items

    return get_all_assignments(api_key, next_url, items)

def get_all_subjects(api_key, ids, url = "https://api.wanikani.com/v2/subjects", subjects = []):
    headers = { "Authorization": "Bearer " + api_key}
    params = { "ids": ids }
    response_json = requests.get(url, params = params, headers = headers).json()
    items = subjects + response_json["data"]
    next_url = response_json["pages"]["next_url"]

    percent = (len(subjects) / int(response_json["total_count"])) * 100
    sys.stdout.write("Loading Subjects [%.2f%%]\r" % (percent))
    sys.stdout.flush()

    if next_url == None:
        return items

    return get_all_subjects(api_key, ids, next_url, items)

