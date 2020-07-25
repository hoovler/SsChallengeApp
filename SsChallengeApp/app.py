"""
app.py: The file containing the application's primary execution
"""
from SsChallengeApp import AppMeta
from pathlib import Path
from datetime import datetime
import pandas as pd


class App:
    """
    App: The class responsible for executing the core application requirements
    """
    # class constants
    LNAME = "lname"
    FNAME = "fname"
    CID = "cid"
    STUDENT = "student"
    TEACHER = "teacher"

    def __init__(self, meta: AppMeta):
        self.meta = meta
        self.initial_fields = ["lname", "fname", "cid"]
        self.student_data = ...
        self.teacher_data = ...

    @classmethod
    def _get_name(cls, data: pd.DataFrame):
        return data[cls.LNAME] + ", " + data[cls.FNAME]

    def load(self):
        """
        Load the initial data into memory; this method takes care to utilize memory resources in a responsible manner,
        and ensures all file handles are closed before the method returns success.
        :return:
        """
        if self.meta.verbose:
            print("in App.load()...")

        # relevant student data...
        data = pd.read_csv(self.meta.students, delimiter="_", usecols=self.initial_fields)
        data["student"] = self._get_name(data)
        self.student_data = data[["student", self.CID]]
        if self.meta.verbose:
            print("--- student data info ---")
            print(f"{self.student_data.agg}")
            print("")

        # relevant teacher data, recycle mem
        data = pd.read_parquet(self.meta.teachers)
        data["teacher"] = self._get_name(data)
        self.teacher_data = data[["teacher", self.CID]]
        if self.meta.verbose:
            print("--- student data info ---")
            print(f"     {self.teacher_data.agg}")
            print("")

        # not necessary, but can't hurt
        del data

    def execute(self):
        """
        Execute the primary requirements of the application
        :return:
        """
        if self.meta.verbose:
            print("in App.execute()...")

        # make output path OS-agnostic
        outpath = Path(self.meta.output_dir)
        outpath.mkdir(parents=True, exist_ok=True)
        outstr = outpath.absolute().__str__()
        if self.meta.verbose:
            print(f"     Output directory created: {outstr}")

        # create filename
        outfile = f"{outstr}/{datetime.now().isoformat(sep='_').replace(':', '.')}_sSChallengeOut.json"

        # merge data, convert to JSON, and write to disks
        self.student_data.merge(self.teacher_data, how='outer').to_json(outfile, orient="records", lines=True)
        if self.meta.verbose:
            print(f"     JSON output written to disk: {outfile}")

    def unload(self):
        """
        Clean remaining memory and close the application
        """
        del self
        exit(0)
