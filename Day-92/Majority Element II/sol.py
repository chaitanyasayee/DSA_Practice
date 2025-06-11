class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_map = {}
        ans = []
        for val in nums:
            if val in  freq_map:
                freq_map[val]+=1
            else:
                freq_map[val]=1
        for key,val in freq_map.items():
            if val > len(nums)/3:
                ans.append(key)
        return ans