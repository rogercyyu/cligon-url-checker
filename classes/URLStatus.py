from classes.Bcolors import Bcolors


class URLStatus:
    """to collect status of URLs"""

    def __init__(self, link, result):
        self.link = link
        self.result = result

    def color(self):
        if self.result == "bad":
            return Bcolors.RED
        elif self.result == "good":
            return Bcolors.GREEN
        else:
            return Bcolors.GREY

    def output(self):
        print(
            self.color()
            + f"{self.result:7}"
            + Bcolors.ENDCOLOR
            + "   ===>   "
            + self.color()
            + self.link
            + Bcolors.ENDCOLOR
        )
