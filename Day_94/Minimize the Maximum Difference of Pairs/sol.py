from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def canFormPairs(maxDiff: int) -> bool:
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i+1] - nums[i] <= maxDiff:
                    count += 1
                    i += 2 
                else:
                    i += 1  
            return count >= p

        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        answer = high

        while low <= high:
            mid = (low + high) // 2
            if canFormPairs(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer
