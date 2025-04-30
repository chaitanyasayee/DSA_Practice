class Solution:
    def isDigit(self,num:int)->bool:
        ans =0
        while(num):
            ans+=1
            num//=10
        return ans %2 ==0
    def findNumbers(self, nums: List[int]) -> int:
        ans =0
        for i in range(len(nums)):
            if self.isDigit(nums[i]) == True:
                ans+=1
        return ans