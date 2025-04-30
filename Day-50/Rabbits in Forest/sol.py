from collections import defaultdict
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        from math import ceil

        count = defaultdict(int)
        for ans in answers:
            count[ans] += 1

        total = 0
        for k, v in count.items():
            group_size = k + 1
            groups = ceil(v / group_size)
            total += groups * group_size

        return total
