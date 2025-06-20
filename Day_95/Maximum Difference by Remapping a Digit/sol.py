class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        max_value = 0
        min_value = num
        for i in set(num_str):
            temp = num_str.replace(i,'9')
            temp2 = num_str.replace(i,'0')
            max_value = max(max_value,int(temp))
            min_value = min(min_value,int(temp2))
        return max_value - min_value
        