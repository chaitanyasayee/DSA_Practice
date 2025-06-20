class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
         n = len(cost)
         ans = [0]*n
         i=0
         temp = 102
         for item in cost:
            if item <temp:
                ans[i] = item
                temp = item
            else:
                ans[i]= temp
            i+=1
         return ans
        