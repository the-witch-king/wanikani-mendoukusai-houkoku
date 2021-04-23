import pandas
import api
from dotenv import dotenv_values, set_key
from datetime import date
from dateutil.relativedelta import relativedelta

ENV_FILE = ".env"
ENV_API_KEY = "WANIKANI_API_KEY"
MONTHS_AGO = 12

def item_date(item):
    return date.fromisoformat(item["data"]["started_at"][:10])

def item_subject_id(item):
    return item["data"]["subject_id"]

def get_user_level(api_key):
    headers = { "Authorization": "Bearer " + api_key }
    response_json = requests.get("https://api.wanikani.com/v2/user", headers = headers).json()
    level = response_json["data"]["level"]
    return level


def make_report_item(assignment, subject):
    return { \
        "characters": subject["data"]["characters"] \
        , "type": subject["object"] \
        , "started": item_date(assignment) \
        , "level": subject["data"]["level"] \
        , "url": subject["data"]["document_url"] \
    }


def build_report(assignments, subjects):
    sorted_assignments = sorted(assignments,key = lambda assignment: assignment["data"]["subject_id"])
    sorted_subjects = sorted(subjects, key = lambda subject: subject["id"])
    total_len = len(sorted_subjects)

    zipped_items = list(zip(sorted_assignments, sorted_subjects))

    return [make_report_item(assignment = item[0], subject = item[1]) for item in zipped_items]


# Check if api key is stored
env_values = dotenv_values(ENV_FILE)
if ENV_API_KEY not in env_values:
    wanikani_api_key = input("Please enter your WaniKani API Key: ")
    set_key(ENV_FILE, ENV_API_KEY, wanikani_api_key)
else:
    wanikani_api_key = env_values[ENV_API_KEY]

# Get all the Assignments
all_items = api.get_all_assignments(wanikani_api_key)
# Filter to ones that are a certain date old
check_from_date = date.today() - relativedelta(months = MONTHS_AGO)
filtered_items = [item for item in all_items if item_date(item) < check_from_date]

# Get all the subjects for the assignments
subject_ids = [item_subject_id(item) for item in filtered_items]
subject_ids_string = (','.join([str(subject_id) for subject_id in subject_ids]))
subjects = api.get_all_subjects(wanikani_api_key, subject_ids_string)

# Make the report!
report = build_report(filtered_items, subjects)

# And done.
df = pandas.DataFrame(report)
df.to_csv("report.csv")
print("Report completed and printed to `report.csv`")
