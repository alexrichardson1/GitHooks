#!/usr/bin/python3

import sys
import re
from colorama import Fore, Style


def exit_failure(error_message):
    print(
        Fore.RED +
        Style.BRIGHT +
        "fatal: " +
        error_message +
        Style.RESET_ALL)
    print("-------------------------------")
    sys.exit(1)


def follows_convention(first_line):
    """Checks if `first_line` follows commit convention"""
    # located in the commit template
    types = ["feat", "fix", "style", "refactor",
             "perf", "test", "docs", "chore", "build", "ci"]
    match = re.match
    if (all([not first_line.startswith(type) for type in types])):
        exit_failure("invalid type.")
    scope = r"[a-z]+\(\.?[\w\-/]+(\.[a-zA-Z]+)?\)"
    if (match(scope, first_line) is None):
        exit_failure("invalid scope.")
    if (match(scope + r": [A-Z]", first_line) is None):
        exit_failure("invalid subject.")
    if len(first_line) > 72:
        exit_failure("header is longer than 72 characters.")
    if (any([first_line.endswith(punc) for punc in [
            ".", "!", "?", "," "...", ":", ";", "(", ")", "'", "-"]])):
        exit_failure("trailing punctuation.")


def update_commit_msg(file):
    new_commit_message = []
    with open(file, "r") as fp:
        lines = fp.readlines()
        if not lines:
            exit_failure("empty commit message.")
        follows_convention(lines[0].lstrip())
        new_commit_message_append = new_commit_message.append
        for line in lines:
            # remove leading whitespace
            if line != "\n":
                line = line.lstrip()
            # ignore comments
            if line.startswith("#"):
                continue
            new_commit_message_append(line)
    fp.close()
    return new_commit_message


def write_commit_msg(file, new_commit_message):
    """Write `new_commit_message` to `file`."""
    with open(file, "w") as fp:
        fp.writelines(new_commit_message)
    fp.close()


def main():
    print("--- Running commit-msg hook ---")
    file = sys.argv[1]
    write_commit_msg(file, update_commit_msg(file))
    print(Fore.GREEN + Style.BRIGHT +
          "Commit-msg hook finished successfully." + Style.RESET_ALL)
    print("-------------------------------")
    sys.exit(0)


if __name__ == "__main__":
    main()
