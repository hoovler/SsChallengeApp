# Technical Challenge App

**Note**: [`SsChallengeApp/scratch.py`](https://github.com/hoovler/SsChallengeApp/blob/master/SsChallengeApp/scratch.py) contains my initial attempt to familiarize myself with the data and complete the primary requirements; it does NOT reflect the final submission.

## Usage

You can run the application directly from the source code, or using application binaries.  All commands herein are intended to be run from your operating system's default shell.  For example, **Windows** users would open the `Command Prompt`, **Mac** users would run them from `Terminal.app`, and **Linux** users would simply pick a terminal.

#### Latest Release

You can find the appropriate executable in the [releases](https://github.com/hoovler/SsChallengeApp/tree/master/releases) directory:
* [v1.0.0, Windows](https://github.com/hoovler/SsChallengeApp/raw/master/releases/v1.0.0/ssChallengeApp.exe) (**_current_**)

Due to the nature of the assignment, it was seemingly impossible to avoid using the `pandas` Python package, which has a major impact on the total size of the binaries packaged into a single executable file.  Even after going through the application's `import` statements to `import` only the necessary classes from required modules, the single-file executable is a hefty **44 MB** in size!

Therefore, since the repository's `release/` page only allows files that are **10 MB** or less, this project repository relies on [Git LFS](https://git-lfs.github.com/) to store the binary executables on GitHub servers using text pointers in the repository itself.

#### Running Directly from Source

To run the application directly from the source code:

1. Clone the repository: `git clone https://github.com/hoovler/SsChallengeApp.git`
2. Navigate into the repository: `cd SsChallengeApp`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the module: `python -m SsChallengeApp <-opts>` (_See the **Arguments** section for `<-opts>`_)

#### Arguments

This table contains all valid arguments into the application and their default values.

| Args | Value | Default | Example | Description |
| ---- | ----- | ------- | ------- | ----------- |
| `-v`, `--verbose` | _NA_ | `False` | `<exec> -v` | Verbosity: if present, print debug logging to the console. |
| `-s`, `--student` | _string filename or URL_ | `data/students.csv` | `<exec> -s https://github.com/singlestone/data_python_exercise/raw/master/data_engineer/students.csv` | Student data source; may use local file or remote URL. |
| `-t`, `--teacher` | _string filename or URL_ | `data/teachers.parquet` | `<exec> -t https://github.com/singlestone/data_python_exercise/raw/master/data_engineer/teachers.parquet` | Teacher data source; may use local file or remote URL. |
| `-o`, `--output_dir` | _string directory_ | `False` | `<exec> -o data/output` | Fully-qualified, local (relative OR absolute) directory for the JSON output.  |
| `-c`, `--chunck_size` | _integer value_ | `False` | `<exec> -o data/output` | The number of records to read at a time from the `student` file.  |

You may also see the arguments and default values with `python -m SsChallengeApp --help`.

#### Examples

**NOTE:** The command used will differ based on the method of execution:
* If running from the source code, `{command}` = `python -m SsChallengeApp`
* From the binary executable, `{command}` = `ssChallengeApp`

The commands used to execute the application vary by operating system and 

If you're low on memory, you can run the application without arguments.  The default `chunk-size` value (_AKA, number of students records stored concurrently in memory_) is `100`:

```batch
> python -m SsChallengeApp -v

verbose: [('-v', '--verbose')] = True
students: [('-s', '--students')] = https://github.com/singlestone/data_python_exercise/raw/master/data_engineer/students.csv
teachers: [('-t', '--teachers')] = https://github.com/singlestone/data_python_exercise/raw/master/data_engineer/teachers.parquet
output_dir: [('-o', '--output_dir')] = output/
chunk_size: [('-c', '--chunk_size')] = 100

in App.execute()...
     chunk #1 with 100 records...
     chunk #2 with 100 records...
     chunk #3 with 100 records...
     chunk #4 with 100 records...
     chunk #5 with 100 records...
     chunk #6 with 100 records...
     chunk #7 with 100 records...
     chunk #8 with 100 records...
     chunk #9 with 100 records...
     chunk #10 with 100 records...
     JSON output streamed to disk: A:\docs\resume\99. Submitted Applications\2020-07-22_KatiBurak_Multiple\SingleStone\SingleStoneChallenge\output/2020-07-27_17.02.17.357094_output.json
```

## Building

The simplest cross-platform method to build the executable binaries is to use `pyinstaller`:

1. Clone the repository: `git clone https://github.com/hoovler/SsChallengeApp.git`
2. Navigate into the repo: `cd SsChallengeApp`
3. Install dependencies: `pip install -r requirements.txt`
4. Build the single executable: `pyinstaller SsChallengeApp\__main__.py -n ssChallengeApp --onefile`

The new executable will be located in the new `dist` directory, as `dist/ssChallengeApp.exe` or `dist/ssChallengeApp.app`.

## Troubleshooting

This section contains some common issues that may arise when executing **Python** applications across different environments.

The following instructions are divided into _`*nix`_ environments (_Linux_, _Unix_, _Mac_) and _`Windows`_ environments. 
The respective terminal commands should be entered into your machine's OS standard shell environment:
* **Linux/Unix**: `terminal`
* **Mac**: `Terminal.app`
* **Windows**: `Command Prompt`


####  1: Check Your Python Installation

Ensure you have `Python 3.6+` installed on your system, and that it's available on your `PATH`.  

**Linux/Unix/Mac**

You can start by executing either:
```bash
$ which python
```


or:

```bash
$ which python3
```

```bash
$ which python
$ which python3
```
If you get `python: aliased to python3`, you're ok to use 

``` 
> python --version
> python3 --version 
```

3. Execute the downloaded release by opening a terminal / command prompt and typing:

```shell
dir> cd SingleStoneChallenge
dir/SingleStoneChallenge> python -m SsChallengeApp
```




```bash
cd /path/to/downloaded/release
python <release_filename> -o <output_directory\>
```

---

## Contributing

Clone the repository and create a branch off `master`

```bash
$ git clone https://github.com/hoovler/SsChallengeApp.git
$ cd SsChallengeApp
$ git checkout -b <branch_name\>
```

### Files



### Run

In order to run the application locally, execute the following from your local terminal (works on Linux, Mac, & Windows):

```bash
$ python3 SsChallengeApp
```

### Build

To build the application into an executable, use `pyinstaller` (`pip install pyinstaller`):

```bash
$ pyinstaller SsChallengeApp\__main__.py -n ssChallengeApp --onefile
```