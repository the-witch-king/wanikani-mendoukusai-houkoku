from utils import item_date
import pandas

class Report:
    def __init__(self, assignments, subjects):
        self.assignments = assignments
        self.subjects = subjects
        self.__build_report()

    def __make_report_item(self, assignment, subject):
        return { \
            "characters": subject["data"]["characters"] \
            , "type": subject["object"] \
            , "started": item_date(assignment) \
            , "level": subject["data"]["level"] \
            , "url": subject["data"]["document_url"] \
        }

    def __build_report(self):
        sorted_assignments = sorted(self.assignments, key = lambda assignment: assignment["data"]["subject_id"])
        sorted_subjects = sorted(self.subjects, key = lambda subject: subject["id"])
        total_len = len(sorted_subjects)

        zipped_items = list(zip(sorted_assignments, sorted_subjects))

        self.report = pandas.DataFrame([self.__make_report_item(assignment = item[0], subject = item[1]) for item in zipped_items])
        return self

    def saveReport(self, path = "report.csv"):
        self.report.to_csv(path)
