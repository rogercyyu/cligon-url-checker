# class to hold URL result and link
from src.Bcolors import Bcolors


class URLstatus:
    """to collect status of URLs"""

    def __init__(self, link, result):
        self.link = link
        self.result = result

    def color(self):
        """colorize the URLs by status"""
        if self.result == "BAD":
            return Bcolors.RED
        elif self.result == "GOOD":
            return Bcolors.GREEN
        else:
            return Bcolors.GREY

    def output(self):
        print(
            self.color()
            + f"{self.result:7}"
            + Bcolors.ENDCOLOR
            + " -> "
            + self.color()
            + self.link
            + Bcolors.ENDCOLOR
        )
