"""
scratch.py
    My initial attempt to familiarize myself with the data files, and complete
    the bare bones requirements (pre-optimization, etc.)
"""
import pandas as pd
from pathlib import Path

STUDENTS = "data/students.csv"
TEACHERS = "data/teachers.parquet"

# read the source files
student_data_full = pd.read_csv(STUDENTS, delimiter="_")
teacher_data_full = pd.read_parquet(TEACHERS)

# pull relevant student info
student_data_full["student"] = student_data_full["lname"] + ", " + student_data_full["fname"]
student_data = student_data_full[["cid", "student"]]

# pull relevant teacher info
teacher_data_full["teacher"] = teacher_data_full["lname"] + ", " + teacher_data_full["fname"]
teacher_data = teacher_data_full[["cid", "teacher"]]

# create merged data
merged_data = student_data.merge(teacher_data, how='outer')

# convert merged set to json
json_data = merged_data.to_json(orient="records", lines=True)


# =============================================================================
# Now, let's optimize!
import pandas as pd
from pathlib import Path

STUDENTS = "data/students.csv"
TEACHERS = "data/teachers.parquet"
OUT_DIR = "output"
Path(OUT_DIR).mkdir(parents=True, exist_ok=True)
OUT_FILE = f"{OUT_DIR}/SsChallengeApp.out"

cols = ["lname", "fname", "cid"]
chunksize = 100

teacher_data = pd.read_parquet(TEACHERS)
teacher_data["teacher"] = teacher_data["lname"] + ", " + teacher_data["fname"]
teacher_data = teacher_data[["cid", "teacher"]]

merged = pd.DataFrame()
with open(OUT_FILE, "a") as file:
    for chunk in pd.read_csv(STUDENTS, delimiter="_", usecols=cols, chunksize=chunksize):
        chunk = pd.DataFrame(chunk)
        chunk["student"] = chunk["lname"] + ", " + chunk["fname"]
        merged = chunk[["student", "cid"]].merge(teacher_data, how="outer")
        file.write(merged.to_json(orient="records"))
    file.close()
