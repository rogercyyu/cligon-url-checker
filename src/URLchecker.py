# This function is used to get any URLs in a file.
# Written in Python 3.8.2
import re
import requests
from src.URLstatus import URLstatus
from src.Bcolors import Bcolors
from src.Counter import Counter
from multiprocessing.dummy import Pool as ThreadPool

class URLchecker:
    # the time it should wait for until it is considered 'timed out' in seconds
    def __init__(self): 
        self.time_out = 2.5
        self.counter = Counter()

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


    def get_url_status(self, link):
        """Get the status code of the URLs, and return URLstatus obj"""
        try:
            status_code = requests.head(link, timeout=self.time_out).status_code
        except requests.exceptions.Timeout:
            status_code = None
        except requests.exceptions.TooManyRedirects:
            status_code = None
        except requests.exceptions.RequestException:
            status_code = None

        if status_code == 404 or status_code == 400:
            result = "BAD"
            self.counter.inc_bad()
        elif status_code == 200:
            result = "GOOD"
            self.counter.inc_good()
        else:
            result = "UNKNOWN"
            self.counter.inc_unknown()

        url_status = URLstatus(link, result)
        return url_status.output()


    def check_url_file(self, file_name):
        """The main function, outputs a list of websites and the result of the website"""
        urls = self.get_URLs_from_file(file_name)

        pool = ThreadPool(10)
        pool.map(self.get_url_status, urls)
        pool.close()
        pool.join()


    def check_url_file_with_counter(self, file_name):
        """The main function, outputs a list of websites and the result of the website with a counter at the end"""
        urls = self.get_URLs_from_file(file_name)

        pool = ThreadPool(10)
        pool.map(self.get_url_status, urls)
        pool.close()
        pool.join()

        # Print out the stats.
        print(
            Bcolors.BOLD
            + "\nURL Check Complete\n"
            + Bcolors.ENDCOLOR
            + f"Good:       {self.counter.good_count:6}\n"
            + f"Bad:        {self.counter.bad_count:6}\n"
            + f"Unknown:    {self.counter.unknown_count:6}\n"
            + f"Total URLs: {self.counter.get_total():6}"
        )