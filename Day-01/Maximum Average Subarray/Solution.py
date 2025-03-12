class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans =0
        avg = 0
        n = len(nums)
        for i in range(k):
            ans+=nums[i]
        avg = ans/k
        for i in range(k,n):
            ans+=nums[i]
            ans-=nums[i-k]
            temp = ans/k
            avg = max(temp,avg)
        return avg        