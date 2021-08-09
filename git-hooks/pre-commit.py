#!/usr/bin/python3

import sys
import os
import subprocess
from colorama import Fore, Back, Style


def run_formatter(file, formatter):
    """Format and stage file."""
    print("Formatting file: " + Back.BLACK + file + Style.RESET_ALL)
    os.system(formatter + file)
    os.system("git add " + file)


def format_files(staged_files, file_extension, formatter):
    """Format `staged_files` with the extension `file_extension` using the command `formatter`."""
    [run_formatter(file, formatter)
     for file in staged_files if file.endswith(file_extension)]


def format_python(files):
    format_files(files, ".py", "autopep8 -i ")


def main():
    print("--- Running pre-commit hook ---")
    files = subprocess.check_output(
        "git diff --name-only --staged",
        shell=True,
        universal_newlines=True)
    staged_files = files.split("\n")
    # add format functions here
    format_functions = [format_python]  # e.g. [format_java, format_haskell]
    [format_function(staged_files) for format_function in format_functions]
    print(Fore.GREEN + Style.BRIGHT +
          "pre-commit hook finished successfully." + Style.RESET_ALL)
    print("-------------------------------")
    sys.exit(0)


if __name__ == "__main__":
    main()
