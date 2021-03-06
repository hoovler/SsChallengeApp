# Data Python Exercise

This exercise is designed to show us your python programming skills.  Although the problem isn't very hard, we would like you to tackle the task the same way you would with a client.  We expect that you provide us with a python application that follows python best practices as defined by the [README](../README.md) at the root of the repository. 

The requirements herein are extracted from the following [Data Python Exercise repository](https://github.com/singlestone/data_python_exercise) files, relative to the root `data_python_excercise` directory:
* [`README.md`](https://github.com/singlestone/data_python_exercise/blob/master/README.md)
* [`data_engineer/README.md`](https://github.com/singlestone/data_python_exercise/blob/master/data_engineer/README.md)
* [`data_engineer/interview_problem.md.encrypted`](https://github.com/singlestone/data_python_exercise/blob/master/data_engineer/interview_problem.md.encrypted)

#### Assumptions

* Application will run on a single machine (not cluster).
    * _Don't worry about multi-tenancy_
* The machine will be somewhat limited in resources.
    * _Consider limited compute, memory, & storage_
* Assume data is too large to be fully loaded into memory.
    * _Stream data from source_

## Requirements

1. Using `students.csv` and `teachers.parquet`, write an application that will **output** a JSON report.  The report should list:
    * each `student` 
    * each student's `teacher`, and
    * each student's `scheduled class ID`
2. Write instructions that explain how to set up and run the application.
    * A `README.md` should be created that explains how to run the application. 
    * a non-developer analyst would be able to setup and run it using only the directions provided

I am going to assume that the proper `JSON` output format will be as such:

```json
[
  {
    "student": "student_a",
    "cid": "cid_a",
    "teacher": "teacher_a"
  },
  {
    "student": "student_b",
    "cid": "cid_a",
    "teacher": "teacher_a"
  },
  {
    "student": "student_c",
    "cid": "cid_a",
    "teacher": "teacher_a"
  },
  {
    "student": "student_n",
    "cid": "cid_n",
    "teacher": "teacher_n"
  }
]
```

#### Architecture
3. All code is organized into python modules.
4. `__main__.py` file with a main function is used as the entry point.
5. code must include a `requirements.txt` file.
6. Unit tests and Integration tests are done to a professional level.


#### Style
7. All code is run through pylint and passes with a 10, **no exceptions**.
8. Notebooks will not be accepted. **no exceptions**. 
9. All code is organized into functions and classes.