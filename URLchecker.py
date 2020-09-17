# This function is used to get any URLs in a file.
# Written in Python 3.8.2

import re
import requests
from classes.URLStatus import URLStatus


def remove_html(text):
    """Remove any html tags, return as string"""
    p = re.compile(r"<.*?>")
    return p.sub("", text)


def get_URLs(file_name):
    """Get URLs using regex, return as an array of strings"""
    regex = r"(?P<url>https?://[^\s]+)"
    fp = open(file_name)
    contents = fp.read()
    return re.findall(regex, remove_html(contents))


def check_file(file_name, time_out):
    """Check the status of the URLs"""
    urls = get_URLs(file_name)

    for link in urls:
        try:
            status_code = requests.get(link, timeout=time_out).status_code
        except requests.exceptions.Timeout:
            status_code = None
        except requests.exceptions.TooManyRedirects:
            status_code = None
        except requests.exceptions.RequestException:
            status_code = None

        # typical cases for a header response
        cases = {404: "bad", 400: "bad", 200: "good"}
        result = cases.get(status_code, "unknown")
        link = URLStatus(link, result)
        link.output()

if __name__ == "__main__":
    print("Error: Please run cligon.py as the main python script.")