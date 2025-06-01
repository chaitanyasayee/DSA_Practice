from math import comb
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        total = comb(n+2,2)
        for i in range(3):
            over = n - (limit +1)
            if over >=0:
                total -= comb(over +2,2)
        over = n-2 *( limit +1)
        if over >=0:
            total += 3 * comb(over +2,2)
        over = n-3 *(limit +1)
        if over >=0:
            total -= comb(over +2,2)
        return total