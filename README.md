# Technical Challenge App

**Note**: [`SsChallengeApp/scratch.py`](https://github.com/hoovler/SsChallengeApp/blob/master/SsChallengeApp/scratch.py) contains my initial attempt to familiarize myself with the data and complete the primary requirements; it does NOT reflect the final submission.

## Usage

1. Download the [latest release](https://github.com/hoovler/SsChallengeApp/releases) for your operating system.
2. Ensure you have `Python 3.6+` available on your `PATH` by opening a terminal / command prompt and typing: 
    * `python --version` or `python3 --version` 
3. Execute the downloaded release by opening a terminal / command prompt and typing: 

```bash
cd /path/to/downloaded/release
python <release_filename> -o <output_directory>
```

## Contributing

Clone the repository and create a branch off `master`

```bash
$ git clone https://github.com/hoovler/SsChallengeApp.git
$ cd SsChallengeApp
$ git checkout -b <branch_name\>
```

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