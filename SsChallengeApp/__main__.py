"""
__main__.py: The file containing the main entry point for the application.
"""
import getopt, sys
from SsChallengeApp import AppMeta, App


def main():
    """
    main: the entry point for the application.
        Arguments may be any order of these long or short arguments followed by the value; default if missing or no value provided
            -s, --students: the local (relative or fully-qualified filename) or remote (URL to raw data) student data;
                    Default="data/students.csv";
            -t, --teachers: the local (relative or fully-qualified filename) or remote (URL to raw data) teacher data;
                    Default="data/teachers.parquet"
            -o, --output: the location to which the JSON output file should be stored;
                    Default="output/"
        And/Or these without any values:
            -v, --verbose: if present, print debug logging to the console
            -h, --help: if present, print application help and exit
    :return: Output to the location determined by the 'output' arg
    """
    short_args = "s:t:o:S:T:uvh"
    long_args = ["students=", "teachers=", "output=", "students_remote=", "teachers_remote=", "update", "verbose", "help"]

    try:
        args, vals = getopt.getopt(sys.argv[1:], short_args, long_args)
    except getopt.error as err:
        print(str(err))
        sys.exit(2)

    # setup the metadata and app from args
    meta = AppMeta(args, vals)
    app = App(meta)

    # and execute the application
    app.load()
    app.execute()
    app.unload()


if __name__ == "__main__":
    main()
