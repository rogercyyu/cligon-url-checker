# This function is used to get any URLs in a file.
# Written in Python 3.8.2
import re
import requests
from src.URLstatus import URLstatus
from multiprocessing.dummy import Pool as ThreadPool

# the time it should wait for until it is considered 'timed out' in seconds
time_out = 2.5


class URLchecker:
    def remove_html_tags(self, text):
        """Remove any html tags, return as string"""
        p = re.compile(r"<.*?>")
        return p.sub("", text)

    def parse_urls_from_file(self, file_name):
        """Get URLs using regex, return as an array of strings"""
        regex = r"(?P<url>https?://[^\s]+)"
        fp = open(file_name)
        contents = fp.read()
        return re.findall(regex, self.remove_html_tags(contents))

    def get_url_status_code(self, link):
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
            result_name = "BAD"
        elif status_code == 200:
            result_name = "GOOD"
        else:
            result_name = "UNKNOWN"

        return URLstatus(link, result_name, status_code)

    def check_urls_thread(self, urls):
        """Check urls by starting threads"""
        pool = ThreadPool(10)
        url_status_list = pool.map(self.get_url_status_code, urls)
        pool.close()
        pool.join()

        return url_status_list

    def output_urls_and_status(self, urls_status_list, args):
        """Outputs a list of websites and the result of the website"""
        output_list = []

        for URLstatus in urls_status_list:
            if args.good and URLstatus.get_result_name() == "GOOD":
                output_list.append(URLstatus)
            elif args.bad and URLstatus.get_result_name() == "BAD":
                output_list.append(URLstatus)
            elif not args.bad and not args.good:
                output_list.append(URLstatus)

        if args.json:
            print("[")
            for i, URLstatus in enumerate(output_list):
                if i:  # print comma if not 0
                    print(",")
                print(URLstatus.output(args), end="")
            print("\n]")
        else:
            for URLstatus in output_list:
                print(URLstatus.output(args))
