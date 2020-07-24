"""
scratch.py
    My initial attempt to familiarize myself with the data files, and complete the bare bones requirements
    (pre-optimization, etc.)
"""
import pandas as pd

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

# TODO: output as json
json_data = merged_data.to_json(orient="records", lines=True)
