#!/usr/bin/env python3
# C.L.I.G.O.N
# Check if Link Is Good Or Not
# Written in Python 3.8.2

import os.path
import sys
from src.URLchecker import URLchecker
import argparse

version = 0.1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?", help="input file")
    parser.add_argument(
        "-v",
        "--version",
        help="Display program name and version number",
        action="store_true",
    )
    parser.add_argument(
        "-c",
        "--counter",
        help="Display a counter of good, bad, and unknown links at the end",
        action="store_true",
    )
    args = parser.parse_args()
    try:
        if args.version:
            print(
                "C.L.I.G.O.N (Check if Link Is Good Or Not) - CLIGON - " + str(version)
            )
        elif args.counter and args.filename:
            checker = URLchecker()
            checker.check_url_file_with_counter(args.filename)
        else:
            checker = URLchecker()
            checker.check_url_file(args.filename)
    except:
        filename = str(args.filename)
        if os.path.isfile(filename) == False:
            print("error: " + filename + " is not a file.")
        else:
            parser.print_help()
        sys.exit(0)


if __name__ == "__main__":
    main()