# Technical Challenge App

**Note**: [`SsChallengeApp/scratch.py`](https://github.com/hoovler/SsChallengeApp/blob/master/SsChallengeApp/scratch.py) contains my initial attempt to familiarize myself with the data and complete the primary requirements; it does NOT reflect the final submission.

## Usage

You can run the application with the source code, or using the released binaries.

#### Running from Source

Open your system's default shell terminal to complete the following steps:

1. Clone the repository: `git clone https://github.com/hoovler/SsChallengeApp.git`
2. Execute it as a module: `python -m SsChallengeApp <-opts>`

#### Running from Binaries
1. Download the [latest release](https://github.com/hoovler/SsChallengeApp/releases).

#### Arguments

Above,`<-opts>` represent the values in this table, which allow the user to customize certain application parameters.

When running the application from the source code, `<exec>` below is `python -m SsChallengeApp`

| Args | Value | Default | Example | Description |
| ---- | ----- | ------- | ------- | ----------- |
| `-v`, `--verbose` | _NA_ | `False` | `<exec> -v` | Verbosity: if present, print debug logging to the console. |
| `-s`, `--student` | _string filename or URL_ | `data/students.csv` | `<exec> -s https://github.com/singlestone/data_python_exercise/raw/master/data_engineer/students.csv` | Student data source; may use local file or remote URL. |
| `-t`, `--teacher` | _string filename or URL_ | `data/teachers.parquet` | `<exec> -t https://github.com/singlestone/data_python_exercise/raw/master/data_engineer/teachers.parquet` | Teacher data source; may use local file or remote URL. |
| `-o`, `--output` | _string directory_ | `False` | `<exec> -o data/output` | Fully-qualified, local (relative OR absolute) directory for the JSON output.  |

You may also see the arguments and default values by executing:

```bash
> python -m SsChallengeApp --help

usage: python -m SsChallenge [('-h', '--help')] [('-v', '--verbose')]
                             [('-s', '--students') <filename>] [('-t', '--teachers') <filename>]
                             [('-o', '--output_dir') <directory>]

If no arguements are provided, the following default values are used:

    Verbose:                'False'
    Student data source:    'data/students.csv'
    Teacher data source:    'data/teachers.parquet'
    Output directory:       'output/'
```

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
python <release_filename> -o <output_directory>
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

To build the application into an executable:

```bash
$ pip install pyinstaller
```