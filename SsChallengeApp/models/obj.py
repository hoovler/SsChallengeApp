"""
obj.py: The with the student and teacher object models
"""
import pandas as pd


class Student:
    """
    Student class: repesenting the student
    """
    def __init__(self, source: str):
        self.source = source
        self.data = self._required_data()

    def _required_data(self):
        temp = pd.read_csv(self.source, delimiter="_")
        temp["student"] = temp["lname"] + ", " + temp["fname"]
        return temp[["cid", "student"]]

    def get_data(self) -> pd.DataFrame:
        """
        Access the student data
        :return: the student dataframe
        """
        return self.data

    def get_source(self) -> str:
        """
        Access the source data file
        :return: the filename of the source data
        """
        return self.source


class Teacher:
    """
    Student class: repesenting the student
    """
    def __init__(self, source: str):
        self.source = source
        self.data = self._required_data()

    def _required_data(self):
        teacher_data_full["teacher"] = teacher_data_full["lname"] + ", " + teacher_data_full["fname"]
        teacher_data = teacher_data_full[["cid", "teacher"]]

        temp = pd.read_csv(self.source, delimiter="_")
        temp["student"] = temp["lname"] + ", " + temp["fname"]
        return temp[["cid", "student"]]

    def get_data(self) -> pd.DataFrame:
        """
        Access the student data
        :return: the student dataframe
        """
        return self.data

    def get_source(self) -> str:
        """
        Access the source data file
        :return: the filename of the source data
        """
        return self.source