class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # findng the first non negative index->number of negaitve numbers
        # finfing tge first postive index which wll eqaul to nums.lenght - that index total pos numbers
        n = len(nums)
        l,r=0,n-1
        while l <=r:
            mid = (l+r)//2
            if nums[mid] <0:
                l = mid + 1
            else:
                r = mid -1
        no_neg = l

        l,r=0,n-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] <= 0:
                l =mid +1
            else:
                r = mid -1
        no_pos = n -l
        return max(no_neg,no_pos)
        