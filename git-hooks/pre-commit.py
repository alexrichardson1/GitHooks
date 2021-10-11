#!/usr/bin/python3

import sys
import os
import subprocess
from colorama import Fore, Back, Style


def exit_failure(error_message):
    print(
        Fore.RED +
        Style.BRIGHT +
        "fatal: " +
        error_message +
        Style.RESET_ALL)
    print("-------------------------------")
    sys.exit(1)


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


def run_linter(file, linter):
    """Lint file."""
    print("Linting file: " + Back.BLACK + file + Style.RESET_ALL)
    os.system(linter + file)
    if os.WEXITSTATUS != 0:
        exit_failure("linting failed")


def lint_files(staged_files, file_extension, linter):
    """Lint `staged_files` with the extension `file_extension` using the command `linter`."""
    [run_linter(file, linter)
     for file in staged_files if file.endswith(file_extension)]


def lint_python(files):
    lint_files(files, ".py", "pylint ")


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
    # add lint functions here
    lint_functions = [lint_python]  # e.g. [lint_java, lint_haskell]
    [lint_function(staged_files) for lint_function in lint_functions]
    print(Fore.GREEN + Style.BRIGHT +
          "pre-commit hook finished successfully." + Style.RESET_ALL)
    print("-------------------------------")
    sys.exit(0)


if __name__ == "__main__":
    main()
