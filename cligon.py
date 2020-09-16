# C.L.I.G.O.N
# Check if Link Is Good Or Not

import requests
import URLchecker
import sys


def main(argv):
    # the time it should wait for until it is considered 'timed out' in seconds
    timeoutSet = 1

    if len(sys.argv) < 2:
        print("cligon: missing operand")
        print("Please add a filename as an argument.")
    else:
        urls = URLchecker.get_URLs(sys.argv[1])

        for link in urls:
            try:
                r = requests.get(link, timeout=timeoutSet).status_code
            except requests.exceptions.Timeout:
                r = None
            except requests.exceptions.TooManyRedirects:
                r = None
            except requests.exceptions.RequestException:
                r = None

            cases = {404: "bad", 400: "bad", 200: "good"}

            print(link + " " + cases.get(r, "unknown"))


if __name__ == "__main__":
    main(sys.argv[1:])