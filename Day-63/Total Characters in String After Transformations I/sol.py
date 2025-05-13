class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        from collections import defaultdict

        # dp[char][time] = number of characters this char produces after `time` transformations
        dp = {chr(c): [0] * (t + 1) for c in range(ord('a'), ord('z') + 1)}

        # Base case: after 0 transformations, each character is itself (length 1)
        for c in dp:
            dp[c][0] = 1

        # Build DP table
        for i in range(1, t + 1):
            for c in range(ord('a'), ord('z') + 1):
                ch = chr(c)
                if ch == 'z':
                    # 'z' becomes 'ab' → sum of dp['a'][i-1] + dp['b'][i-1]
                    dp[ch][i] = (dp['a'][i - 1] + dp['b'][i - 1]) % MOD
                else:
                    next_ch = chr(c + 1)
                    dp[ch][i] = dp[next_ch][i - 1]

        # Compute final length
        result = 0
        for ch in s:
            result = (result + dp[ch][t]) % MOD

        return result
