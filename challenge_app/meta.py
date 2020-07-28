"""
meta.py: The file containing the metadata for the student and teacher models
"""
from collections import namedtuple
from sys import exit


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
    _s = _Arg(("-s", "--students"), f"{_REMOTE_REPO}/{_STUDENT_FILE}")
    _t = _Arg(("-t", "--teachers"), f"{_REMOTE_REPO}/{_TEACHER_FILE}")
    _o = _Arg(("-o", "--output_dir"), f"{_OUTPUT_DIR}/")
    _c = _Arg(("-c", "--chunk_size"), 100)

    def __init__(self, args):
        """
        Parse the args (other than -h, --help)
        :param args:
        """

        # set default class variables and add to param list
        self.help = self._h.default
        self.verbose = self._v.default
        self.students = self._s.default
        self.teachers = self._t.default
        self.output_dir = self._o.default
        self.chunk_size = self._c.default

        print("=========args=========")
        print(args)
        print("")

        if args is not None:
            # evaluate arguments
            for this_arg, this_val in args:
                if this_arg in self._h.switches:
                    self.show_help()
                    exit(0)
                elif this_arg in self._v.switches:
                    self.verbose = True
                elif this_arg in self._s.switches:
                    self.students = this_val
                elif this_arg in self._t.switches:
                    self.teachers = this_val
                elif this_arg in self._o.switches:
                    self.output_dir = this_val
                elif this_arg in self._c.switches:
                    self.chunk_size = int(this_val)
                else:
                    if self.verbose:
                        print("no known args... using defaults; to see args list, use:")
                        print("                  python -m challenge_app --help")
        else:
            # defaults already set...
            pass

        # respect verbosity arg
        if self.verbose:
            self.show_meta()

    def show_meta(self):

        """
        printMeta: print the application metdata to the console.
        :return:
        """
        print("")
        # print(f"    Verbose [-v]:               '{self.verbose}'")
        # print(f"    Student data source [-s]:   '{self.students}'")
        # print(f"    Teacher data source [-f]:   '{self.teachers}'")
        # print(f"    Output directory [-o]:      '{self.output_dir}'")
        # print(f"    Chunk size [-c]:            '{self.chunk_size}'")
        for key in self.as_dict().keys():
            val = self.as_dict().get(key)
            print(f"{key}: [{val[1].switches}] = {val[0]}")
        print("")

    def show_help(self):
        """
        help: print help information to the console
        """
        print("")
        print(f"usage: python -m SsChallenge [{self._h.switches}] [{self._v.switches}]")
        print(f"                             [{self._s.switches} <filename>] "
              f"[{self._t.switches} <filename>] "
              f"[{self._o.switches} <directory>]")
        print(f"                             [{self._c.switches} <int>]")
        print("")
        print("If no arguements are provided, the following default values are used:")
        self.show_meta()

    def as_dict(self) -> dict:
        """
        Convert application metadata into a dictionary
        :return: {verbose:v, students:s, teachers:t, output_dir:o}
        """
        return {
            "verbose": [self.verbose, self._v],
            "students": [self.students, self._s],
            "teachers": [self.teachers, self._t],
            "output_dir": [self.output_dir, self._o],
            "chunk_size": [self.chunk_size, self._c]
        }

    def as_list(self):
        """
        Convert application metadata into a list
        :return: [self.verbose, self.students, self.teachers, self.output_dir]
        """
        return [self.verbose, self.students, self.teachers, self.output_dir, self.chunk_size]
