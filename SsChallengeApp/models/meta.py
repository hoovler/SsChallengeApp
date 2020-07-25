"""
meta.py: The file containing the metadata for the student and teacher models
"""
from collections import namedtuple
import sys


class AppMeta:
    """
    AppMeta: Values to use throughout application runtime.
    """
    # app default constants
    _REMOTE_REPO = "https://github.com/singlestone/data_python_exercise/raw/master/data_engineer"
    _STUDENT_FILE = "students.csv"
    _TEACHER_FILE = "teachers.parquet"
    _INPUT_DIR = "data"
    _OUTPUT_DIR = "output"

    # set up namedtuple to hold arguments
    _Arg = namedtuple("Arg", ["switches", "default"])

    # create expected args and default values
    _h = _Arg(("-h", "--help"), False)
    _v = _Arg(("-v", "--verbose"), False)
    _s = _Arg(("-s", "--students"), f"{_INPUT_DIR}/{_STUDENT_FILE}")
    _t = _Arg(("-t", "--teachers"), f"{_INPUT_DIR}/{_TEACHER_FILE}")
    _o = _Arg(("-o", "--output_dir"), f"{_OUTPUT_DIR}/")

    def __init__(self, args, vals):
        """
        Parse the args (other than -h, --help)
        :param args:
        """

        # set default class variables
        self.help = self._h.default
        self.verbose = self._v.default
        self.students = self._s.default
        self.teachers = self._t.default
        self.output_dir = self._o.default

        # evaluate arguments
        for this_arg, this_val in args:
            if this_arg in self._h.switches:
                self.show_help()
                sys.exit(0)
            elif this_arg in self._v.switches:
                self.verbose = True
            elif this_arg in self._s.switches:
                self.students = this_val
            elif this_arg in self._t.switches:
                self.teachers = this_val
            elif this_arg in self._o.switches:
                self.output_dir = this_val
            else:
                if self.verbose:
                    print("no known args... using defaults; to see args list, use:")
                    print("                  python -m SsChallengeApp --help")

        # respect verbosity arg
        if self.verbose:
            self.show_meta()

    def show_meta(self):
        """
        printMeta: print the application metdata to the console.
        :return:
        """
        print("")
        print(f"    Verbose:                '{self.verbose}'")
        print(f"    Student data source:    '{self.students}'")
        print(f"    Teacher data source:    '{self.teachers}'")
        print(f"    Output directory:       '{self.output_dir}'")
        print("")

    def show_help(self):
        """
        help: print help information to the console
        """
        print("")
        print(f"usage: python -m SsChallenge [{self._h.switches}] [{self._v.switches}]")
        print(f"                             [{self._s.switches} <filename>] [{self._t.switches} <filename>]")
        print(f"                             [{self._o.switches} <directory>]")
        print("")
        print("If no arguements are provided, the following default values are used:")
        self.show_meta()

    def as_dict(self):
        """
        Convert application metadata into a dictionary
        :return: {verbose:v, students:s, teachers:t, output_dir:o}
        """
        return {
            "verbose": self.verbose,
            "students": self.students,
            "teachers": self.teachers,
            "output_dir": self.output_dir
        }

    def as_list(self):
        """
        Convert application metadata into a list
        :return: [self.verbose, self.students, self.teachers, self.output_dir]
        """
        return [self.verbose, self.students, self.teachers, self.output_dir]