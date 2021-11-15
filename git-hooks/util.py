"""
Utility functions.
"""

import sys
from colorama import Fore, Style


def print_successful(hook_name):
    """Print that `hook_name` has finished successfully."""
    print(Fore.GREEN + Style.BRIGHT +
          f"{hook_name} hook finished successfully." + Style.RESET_ALL)


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
