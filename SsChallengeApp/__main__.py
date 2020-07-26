"""
__main__.py: The file containing the main entry point for the application.
"""
import getopt
import sys
from SsChallengeApp import AppMeta, App


def main():
    """
    main: the entry point for the application.
        Arguments may be any order of these long or short arguments followed by the value;
        default if missing or no value provided
            -s, --students: the local (relative or fully-qualified filename) or remote
                    (URL to raw data) student data; Default="data/students.csv"
            -t, --teachers: the local (relative or fully-qualified filename) or remote
                    (URL to raw data) teacher data; Default="data/teachers.parquet"
            -o, --output: the location to which the JSON output file should be stored;
                    Default="output/"
            -c, --chunk_size: the number of student records to process at once;
                    Default=100
        And/Or these without any values:
            -v, --verbose: if present, print debug logging to the console
            -h, --help: if present, print application help and exit
    :return: Output to the location determined by the 'output' arg
    """
    short_args = "s:t:o:c:vh"
    long_args = ["students=", "teachers=", "output=", "chunk_size=", "verbose", "help"]

    try:
        # pylint incorrectly assumes 'vals' is unused - it's packaged with
        # 'args' and sent to AppMeta(args)
        args, vals = getopt.getopt(sys.argv[1:], short_args, long_args)
    except getopt.error as err:
        print(str(err))
        sys.exit(2)

    # setup the metadata and app from args, and execute
    meta = AppMeta(args)
    app = App(meta)
    app.execute()


if __name__ == "__main__":
    main()
