class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        l=0
        numswap = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                numswap+=1
            while ( numswap > k):
                if nums[l] == 0:
                    numswap-=1
                l+=1
            curr_length = i - l+1
            max_length = max(curr_length,max_length)
        return max_length