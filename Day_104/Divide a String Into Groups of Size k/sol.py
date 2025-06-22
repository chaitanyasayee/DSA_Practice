class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        i =0
        n = len(s)
        while (i<n):
            group = s[i:i+k]
            if len(group)<k:
                group+=(fill*(k-len(group)))
            ans.append(group)
            i+=k
        return ans