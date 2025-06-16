class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans =-1
        for i in range(n):
            for j in range(i,n):
                if nums[j] > nums[i]:
                    ans = max(nums[j] - nums[i],ans)
        return ans