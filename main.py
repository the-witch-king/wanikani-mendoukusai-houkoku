from report import Report
from api import WaniKaniApi
from utils import *
from dotenv import dotenv_values, set_key


ENV_FILE = ".env"
ENV_API_KEY = "WANIKANI_API_KEY"
MONTHS_AGO = 12

# Check if api key is stored
env_values = dotenv_values(ENV_FILE)
if ENV_API_KEY not in env_values:
    wanikani_api_key = input("Please enter your WaniKani API Key: ")
    set_key(ENV_FILE, ENV_API_KEY, wanikani_api_key)
else:
    wanikani_api_key = env_values[ENV_API_KEY]

# Our wonderful API
api = WaniKaniApi(wanikani_api_key)

# Get all the Assignments
all_assignments = api.get_all_assignments()

# Filter to ones that are a certain date old
filtered_assignments = filter_assignments_by_date(all_assignments, months_from_today(MONTHS_AGO))

# Get all the subjects for the assignments
subject_ids_string = subject_ids_to_string(get_subject_ids_from_assignments(filtered_assignments))
subjects = api.get_all_subjects(subject_ids_string)

# Make the report!
report = Report(filtered_assignments, subjects).saveReport()

# All done!
print("Report completed and printed to `report.csv`")
