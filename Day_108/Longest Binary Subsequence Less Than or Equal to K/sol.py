class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        curr = length = 0
        for c in s[::-1]:
            if c == '0':
                length+=1
            elif (curr | 1<<length) <= k:
                curr |= 1<<length
                length += 1
        return length