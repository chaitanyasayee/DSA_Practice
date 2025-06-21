class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = {}
        for w in word:
            if w not in freq:
                freq[w] = 1
            else:
                freq[w] += 1
        
        min_deletions = float('inf')
        max_freq = max(freq.values())

        for target in range(1, max_freq + 1):
            deletions = 0
            for f in freq.values():
                if f < target:
                    deletions += f
                elif f > target + k:
                    deletions += f - (target + k)
            min_deletions = min(min_deletions, deletions)

        return min_deletions
