from src.TerminalColors import TerminalColors


class URLstatus:
    """to collect status of URLs"""

    def __init__(self, link, result, code):
        self.link = link
        self.result = result
        self.code = code

    def color(self):
        """colorize the URLs by status"""
        if self.result == "BAD":
            return TerminalColors.RED
        elif self.result == "GOOD":
            return TerminalColors.GREEN
        else:
            return TerminalColors.GREY

    def output(self, args):
        if args.json:
            print(
                '{ "url": "' + self.link + '", "status": "' + str(self.code) + '" },',
                file=open("output.json", "a"),
            )
        else:
            print(
                self.color()
                + f"{self.result:7}"
                + TerminalColors.ENDCOLOR
                + " -> "
                + self.color()
                + self.link
                + TerminalColors.ENDCOLOR
            )