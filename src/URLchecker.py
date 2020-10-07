# This function is used to get any URLs in a file.
# Written in Python 3.8.2
import re
import requests
from src.URLstatus import URLstatus
from multiprocessing.dummy import Pool as ThreadPool
from itertools import repeat


# the time it should wait for until it is considered 'timed out' in seconds
time_out = 2.5


class URLchecker:
    def remove_html(self, text):
        """Remove any html tags, return as string"""
        p = re.compile(r"<.*?>")
        return p.sub("", text)

    def get_URLs_from_file(self, file_name):
        """Get URLs using regex, return as an array of strings"""
        regex = r"(?P<url>https?://[^\s]+)"
        fp = open(file_name)
        contents = fp.read()
        return re.findall(regex, self.remove_html(contents))

    def get_url_status(self, link, args):
        """Get the status code of the URLs, and outputs a list of URLstatus obj"""
        try:
            status_code = requests.head(link, timeout=time_out).status_code
        except requests.exceptions.Timeout:
            status_code = None
        except requests.exceptions.TooManyRedirects:
            status_code = None
        except requests.exceptions.RequestException:
            status_code = None

        if status_code == 404 or status_code == 400:
            result = "BAD"
        elif status_code == 200:
            result = "GOOD"
        else:
            result = "UNKNOWN"

        url_status = URLstatus(link, result)

        if args.good and result == "GOOD":
            url_status.output()
        elif args.bad and result == "BAD":
            url_status.output()
        elif not args.bad and not args.good:
            url_status.output()

    def check_url_file(self, file_name, args):
        """The main function, outputs a list of websites and the result of the website"""
        urls = self.get_URLs_from_file(file_name)

        pool = ThreadPool(10)
        pool.starmap(self.get_url_status, zip(urls, repeat(args)))
        pool.close()
        pool.join()
