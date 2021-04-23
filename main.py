from report import Report
from api import WaniKaniApi
from utils import *
from dotenv import dotenv_values, set_key
import argparse

ENV_FILE = ".env"
ENV_API_KEY_INDEX = "WANIKANI_API_KEY"
MONTHS_AGO = 12
SAVE_PATH = "report.csv"
API_KEY = None

parser = argparse.ArgumentParser()

parser.add_argument("-o", "--out", help="Path to save report csv to.")
parser.add_argument("-k", "--key", help="WaniKani API Key")
parser.add_argument("-m", "--months", help="Minimum amount of months since learning an item (default is 12)")

args = parser.parse_args()
if args.out:
    SAVE_PATH = args.out
if args.key:
    API_KEY = args.key
if args.months:
    MONTHS_AGO = int(args.months)

# Check if api key is stored
if not API_KEY:
    env_values = dotenv_values(ENV_FILE)
    if ENV_API_KEY_INDEX not in env_values:
        API_KEY = input("Please enter your WaniKani API Key: ")
        set_key(ENV_FILE, ENV_API_KEY_INDEX, API_KEY)
    else:
        API_KEY = env_values[ENV_API_KEY_INDEX]

# Our wonderful API
api = WaniKaniApi(API_KEY)

# Get all the Assignments
all_assignments = api.get_all_assignments()

# Filter to ones that are a certain date old
filtered_assignments = filter_assignments_by_date(all_assignments, months_from_today(MONTHS_AGO))

# Get all the subjects for the assignments
subject_ids_string = subject_ids_to_string(get_subject_ids_from_assignments(filtered_assignments))
subjects = api.get_all_subjects(subject_ids_string)

# Make the report!
report = Report(filtered_assignments, subjects).saveReport(SAVE_PATH)

# All done!
print("Report completed and printed to `report.csv`")
