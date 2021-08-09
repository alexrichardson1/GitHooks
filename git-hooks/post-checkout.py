#!/usr/bin/python3

import os
import sys
from colorama import Fore, Style


def main():
    print("--- Running post-checkout hook ---")
    CLEAN_COMMAND = ""
    os.system(CLEAN_COMMAND)  # clean command here e.g. `make clean`
    print(Fore.GREEN + Style.BRIGHT +
          "post-checkout hook finished successfully." + Style.RESET_ALL)
    print("-------------------------------")
    sys.exit(0)


if __name__ == "__main__":
    main()
