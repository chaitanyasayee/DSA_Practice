class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans =[]
        result =set()
        n = len(nums)-1
        for i,num in enumerate(nums):
            if num ==key:
                start = max(0,i-k)
                end = min(n,i+k)
                for a in range(start,end+1):
                    result.add(a)
        return list(result)
