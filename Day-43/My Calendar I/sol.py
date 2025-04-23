
from sortedcontainers import SortedDict

class MyCalendar:
    def __init__(self):
        self.sd = SortedDict()

    def book(self, start: int, end: int) -> bool:
        # bisect_left will not work, due to duplicates
        # eg: [[],[10,20],[15,25],[20,30]]
        idx = self.sd.bisect_right(start)

        # self.sd.keys()[idx] ==> end time
        # self.sd.values()[idx] ==> it's start time
        if idx < len(self.sd) and end > self.sd.values()[idx]:
            return False
        self.sd[end] = start
        return True