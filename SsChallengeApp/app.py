"""
app.py: The file containing the application's primary execution
"""
from pathlib import Path
from datetime import datetime
from SsChallengeApp import AppMeta
from pandas import DataFrame, read_parquet, read_csv


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
        self.success = False
        self.initial_fields = ["lname", "fname", "cid"]
        self.student_data = ...
        self.teacher_data = ...

    @classmethod
    def _get_name(cls, data: DataFrame):
        return data[cls.LNAME] + ", " + data[cls.FNAME]

    def is_success(self):
        """
        Validate whether the application executed completely and successfully
        :return: True if application finished without issues
        """
        return self.success

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

        # create filename
        outfile = f"{outstr}/{datetime.now().isoformat(sep='_').replace(':', '.')}_output.json"

        # load up the teacher data (1 time only)
        t_data = read_parquet(self.meta.teachers)
        t_data["teacher"] = self._get_name(t_data)
        t_data = t_data[["cid", "teacher"]]

        # init loop count
        chunk_num = 0

        # open output file for writing; Pandas.DF doesn't support output streaming
        # or appending to files
        with open(outfile, "a") as file:
            # start chunking in student data (for chunk_size/total_size iterations)
            for chunk in read_csv(self.meta.students,
                                  delimiter="_",
                                  usecols=self.initial_fields,
                                  chunksize=self.meta.chunk_size):
                chunk_num += 1
                chunk = DataFrame(chunk)
                chunk["student"] = chunk["lname"] + ", " + chunk["fname"]
                # merge data, convert to JSON, and append to output file
                file.write(chunk[["student", "cid"]]
                           .merge(t_data, how="outer").to_json(orient="records"))
                # process loop count
                if self.meta.verbose:
                    print(f"     chunk #{chunk_num} with {len(chunk)} records...")
            # close file after all chunks are processed
            file.close()

        # inform the user!
        if self.meta.verbose:
            print(f"     JSON output streamed to disk: {outfile}")
        self.success = True
