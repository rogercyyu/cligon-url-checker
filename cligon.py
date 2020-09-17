# C.L.I.G.O.N
# Check if Link Is Good Or Not
# Written in Python 3.8.2

import URLchecker
import sys

version = 0.1

# TODO: Change to Python Built in library Argparse.
def main(argv):
    # the time it should wait for until it is considered 'timed out' in seconds
    time_out = 1

    # check types of arguments
    if len(sys.argv) < 2:
        print(
            "cligon: cligon [version or filename]\n"
            "    Checks and displays the status of URL links inside of a file specified by the user.\n"
            "    If no argument is specified, this default message is displayed.\n\n"
            "    Options:\n"
            "       v or --version    Display program name and version number\n\n"
            "    Arguments:\n"
            "       [FILENAME]        The file of which to check URL link status"
        )
    elif sys.argv[1] == "v" or sys.argv[1] == "--version":
        print("C.L.I.G.O.N (Check if Link Is Good Or Not) - CLIGON - " + str(version))
    else:
        # run URL scraper
        try:
            URLchecker.check_file(sys.argv[1], time_out)
        except FileNotFoundError:
            print("cligon: File not found.")


if __name__ == "__main__":
    main(sys.argv[1:])