#!/usr/bin/python3
# pylint: disable=C0103
"""
pre-commit hook is used to inspect the snapshot that’s about to be committed
"""

import sys
import os
import subprocess
from colorama import Fore, Back, Style


def exit_failure(error_message):
    """Exits non-zero with error message."""
    print(
        Fore.RED +
        Style.BRIGHT +
        "fatal: " +
        error_message +
        Style.RESET_ALL)
    print("-------------------------------")
    sys.exit(1)


def run_formatter(files, formatter):
    """Format and stage files."""
    files_list = [f for f in files.split(" ") if f != ""]
    for file in files_list:
        print("Formatting file: " + Back.BLACK + file + Style.RESET_ALL)
    os.system(formatter + files)
    os.system("git add " + files)


def format_files(staged_files, file_extension, formatter):
    """Format `staged_files` with the extension `file_extension` using the command `formatter`."""
    files = ""
    for file in staged_files:
        if file.endswith(file_extension):
            files += f"{file} "
    if files != "":
        run_formatter(files, formatter)


def format_python(files):
    """Formats python files"""
    format_files(files, ".py", "autopep8 -i ")


def run_linter(files, linter):
    """Lint `file` using the command `linter`."""
    files_list = [f for f in files.split(" ") if f != ""]
    for file in files_list:
        print("Linting file: " + Back.BLACK + file + Style.RESET_ALL)
    if os.WEXITSTATUS(os.system(linter + files)) != 0:
        exit_failure("linting failed")


def lint_files(staged_files, file_extension, linter):
    """Lint `staged_files` with the extension `file_extension` using the command `linter`."""
    files = ""
    for file in staged_files:
        if file.endswith(file_extension):
            files += f"{file} "
    if files != "":
        run_linter(files, linter)


def lint_python(files):
    """Lint python files."""
    lint_files(files, ".py", "pylint ")


def main():
    """Main function for the pre-commit hook."""
    print("--- Running pre-commit hook ---")
    files = subprocess.check_output(
        "git diff --name-only --staged",
        shell=True,
        universal_newlines=True)
    staged_files = files.split("\n")
    files = subprocess.check_output(
        "git diff --name-only --diff-filter=D",
        shell=True,
        universal_newlines=True)
    deleted_filles = files.split("\n")
    staged_files = [
        file for file in staged_files if file not in deleted_filles]
    # add format functions here
    format_functions = [format_python]  # e.g. [format_java, format_haskell]
    for format_function in format_functions:
        format_function(staged_files)
    # add lint functions here
    lint_functions = [lint_python]  # e.g. [lint_java, lint_haskell]
    for lint_function in lint_functions:
        lint_function(staged_files)
    print(Fore.GREEN + Style.BRIGHT +
          "pre-commit hook finished successfully." + Style.RESET_ALL)
    print("-------------------------------")
    sys.exit(0)


if __name__ == "__main__":
    main()
