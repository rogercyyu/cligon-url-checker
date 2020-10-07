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
    parser.add_argument("filename", nargs="?", help="input file to check URL links")
    parser.add_argument(
        "-v",
        "--version",
        help="display program name and version number",
        action="version",
        version="C.L.I.G.O.N (Check if Link Is Good Or Not) - CLIGON - " + str(version),
    )
    parser.add_argument(
        "-j", "--json", action="store_true", help="output program results into a JSON file"
    )
    args = parser.parse_args()
    try:
        checker = URLchecker()
        checker.check_url_file(args.filename, args)
    except:
        filename = str(args.filename)
        if os.path.isfile(filename) == False and not filename:
            print("error: " + filename + " is not a file.")
        else:
            parser.print_help()
        sys.exit(0)


if __name__ == "__main__":
    main()