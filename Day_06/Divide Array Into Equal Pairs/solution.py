class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        occurence_map = {}
        for num in nums:
            if num in occurence_map:
                occurence_map[num]+=1
            else:
                occurence_map[num]=1
        for occurence in occurence_map.values():
            # print(occurence)
            if occurence %2 != 0:
                return False
        return True
        