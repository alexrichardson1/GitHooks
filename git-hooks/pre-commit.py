#!/usr/bin/python3
# pylint: disable=C0103
# pylint: disable=R1729
"""
pre-commit hook is used to inspect the snapshot that’s about to be committed
"""

import sys
import os
import subprocess
from colorama import Back, Style
from util import exit_failure, print_successful


def run_formatter(files, formatter):
    """Format and stage files."""
    files_list = [f for f in files.split(" ") if f != ""]
    for file in files_list:
        print("Formatting file: " + Back.BLACK + file + Style.RESET_ALL)
    if os.WEXITSTATUS(os.system(formatter + files)) != 0:
        exit_failure("formatting failed")
    os.system("git add " + files)


def format_files(staged_files, file_extensions, formatter):
    """Format `staged_files` with the extension `file_extension` using the command `formatter`."""
    files = ""
    for file in staged_files:
        if any([file.endswith(file_extension)
                for file_extension in file_extensions]):
            files += f"{file} "
    if files != "":
        run_formatter(files, formatter)


def format_python(files):
    """Formats python files"""
    format_files(files, [".py"], "autopep8 -i ")


def run_linter(files, linter):
    """Lint `file` using the command `linter`."""
    files_list = [f for f in files.split(" ") if f != ""]
    for file in files_list:
        print("Linting file: " + Back.BLACK + file + Style.RESET_ALL)
    if os.WEXITSTATUS(os.system(linter + files)) != 0:
        exit_failure("linting failed")


def lint_files(staged_files, file_extensions, linter):
    """Lint `staged_files` with the extension `file_extension` using the command `linter`."""
    files = ""
    for file in staged_files:
        if any([file.endswith(file_extension)
                for file_extension in file_extensions]):
            files += f"{file} "
    if files != "":
        run_linter(files, linter)


def lint_python(files):
    """Lint python files."""
    lint_files(files, [".py"], "pylint ")


def main():
    """Main function for the pre-commit hook."""
    print("--- Running pre-commit hook ---")
    # all staged files except delted files
    files = subprocess.check_output(
        "git diff --name-only --staged --diff-filter=d",
        shell=True,
        universal_newlines=True)
    staged_files = [file for file in files.split("\n") if file != ""]
    # add format functions here
    format_functions = [format_python]  # e.g. [format_java, format_haskell]
    for format_function in format_functions:
        format_function(staged_files)
    # add lint functions here
    lint_functions = [lint_python]  # e.g. [lint_java, lint_haskell]
    for lint_function in lint_functions:
        lint_function(staged_files)
    print_successful("pre-commit")
    print("-------------------------------")
    sys.exit(0)


if __name__ == "__main__":
    main()
