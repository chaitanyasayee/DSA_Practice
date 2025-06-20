class Solution:
    def maxDifference(self, s: str) -> int:
        alphabet_count = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        for char in s:
            alphabet_count[char]+=1
        values = alphabet_count.values()
        odd_freqs = (v for v in values if v % 2 == 1)
        even_freqs = (v for v in values if v % 2 == 0 and v != 0)
        
        if odd_freqs and even_freqs:
            return max(odd_freqs) - min(even_freqs)
        else:
            # No valid a1 or a2 found
            return -1
