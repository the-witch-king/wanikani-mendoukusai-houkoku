from datetime import date
from dateutil.relativedelta import relativedelta

def item_date(item):
    return date.fromisoformat(item["data"]["started_at"][:10])

def item_subject_id(item):
    return item["data"]["subject_id"]

def months_from_today(months):
    return date.today() - relativedelta(months = months)

def filter_assignments_by_date(assignments, earliest_date):
    return [item for item in assignments if item_date(item) < earliest_date]

def get_subject_ids_from_assignments(assignments):
    return [item_subject_id(item) for item in assignments]

def subject_ids_to_string(subject_ids):
    return (','.join([str(subject_id) for subject_id in subject_ids]))



