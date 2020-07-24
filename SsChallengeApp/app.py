"""
app.py
"""
import csv


class Student:
    """
    Student class
    """

    keys = {
        "student_id": "id",
        "firstname": "fname",
        "lastname": "lname",
        "email": "email",
        "ssn": "ssn",
        "address": "address",
        "course_id": "cid"
    }

    def __init__(self, source, delim="_", quotation=csv.QUOTE_NONE, update=False):
        """
        :param source: The source file containing student data.
        :param delim: The delimiter character used to separate values. *Optional, default="_"*
        :param quotation: The quote character used to group values the might contain the delimiter; *Optional, default=csv.QUOTE_NONE*
        :param update: If `True`, will pull a fresh copy of the data from its Github repository; *Optional, default=False*
        """
        self.update = update
        self.source = source
        self.delim = delim
        self.quotation = quotation

    def _get_value(self, row, column):
        pass

    def _get_all(self):
        pass

    def _open_reader(self):
        with open(self.source, 'rb') as f:
            return csv.reader(f, self.source, delimiter=self.delim, quoting=self.quotation)

    @property
    def firstname(self):
        return _get_value(student_id, self.keys["firstname"])



class Teacher:
    """
    Teacher class
    """
    def __init__(self, source):
        self.source = source
