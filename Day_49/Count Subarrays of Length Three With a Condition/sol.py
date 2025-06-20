class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums) -1
        ans,i =0,0
        while(i<n-1):
            j=i+1
            if nums[i] + nums[j+1] == nums[j]/2:
                ans+=1
            i+=1
        return ans