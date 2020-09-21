#!/usr/bin/env python3
# C.L.I.G.O.N
# Check if Link Is Good Or Not
# Written in Python 3.8.2

from src.URLchecker import *
import sys

version = 0.1

# TODO: Change to Python Built in library Argparse.
def main(argv):
    # check types of arguments
    if len(sys.argv) < 2:
        print(
            "cligon: cligon [options] [version or filename]\n"
            "    Checks and displays the status of URL links inside of a file specified by the user.\n"
            "    If no argument is specified, this default message is displayed.\n\n"
            "    Options:\n"
            "       -v or --version    Display program name and version number\n"
            "       -c or --counter    Display a counter of good, bad, and unknown links at the end\n\n"
            "    Arguments:\n"
            "       [FILENAME]        The file of which to check URL link status"
        )
    elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
        print("C.L.I.G.O.N (Check if Link Is Good Or Not) - CLIGON - " + str(version))
    elif sys.argv[1] == "-c" or sys.argv[1] == "--counter":
        # run URL scraper
        try:
            check_url_file_with_counter(sys.argv[2])
        except FileNotFoundError:
            print("cligon: File not found. Or command not recognized.")
    else:
        # run URL scraper
        try:
            check_url_file(sys.argv[1])
        except FileNotFoundError:
            print("cligon: File not found. Or command not recognized.")


if __name__ == "__main__":
    main(sys.argv[1:])