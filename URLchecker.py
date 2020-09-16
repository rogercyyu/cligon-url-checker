# This function is used to get any URLs in a file.
import re

regex = r"(?P<url>https?://[^\s]+)"


def remove_html(text):
    p = re.compile(r"<.*?>")
    return p.sub("", text)


def get_URLs(file_name):
    fp = open(file_name)
    contents = fp.read()
    return re.findall(regex, remove_html(contents))


if __name__ == "__main__":
    print("Error: Please run cligon.py as the main python script.")