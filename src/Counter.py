# This class is used to keep count of good, bad, unknown URLs
class Counter:
    good_count = 0
    unknown_count = 0
    bad_count = 0

    def increase_good(self):
        self.good_count += 1

    def increase_bad(self):
        self.bad_count += 1

    def increase_unknown(self):
        self.unknown_count += 1

    def get_total(self):
        return self.bad_count + self.good_count + self.unknown_count
