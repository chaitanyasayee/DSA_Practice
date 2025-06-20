class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0

        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break  # Stop if a duplicate is found
                seen.add(s[j])
                longest = max(longest, j - i + 1)

        return longest
