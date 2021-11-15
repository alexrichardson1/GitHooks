#!/usr/bin/python3
# pylint: disable=C0103
"""
post-checkout hook is used to perform repository validity checks
"""

import os
import sys
from util import print_successful


def main():
    """Main function for the post-checkout hook."""
    print("--- Running post-checkout hook ---")
    command = ""
    os.system(command)  # clean command here e.g. `make clean`
    print_successful("post-checkout")
    print("-------------------------------")
    sys.exit(0)


if __name__ == "__main__":
    main()
