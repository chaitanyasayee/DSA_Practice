class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        def max_num(num_str)-> int:
            for ch in num_str:
                if ch !='9':
                    return int(num_str.replace(ch,'9'))
            return int(num_str)
        def min_num(num_str)->int:
            if num_str[0] != '1':
                return int(num_str.replace(num_str[0],'1'))
            else:
                for ch in num_str[1:]:
                    if ch != '0' and ch!='1':
                        return int(num_str.replace(ch,'0'))
                return int(num_str)
            
        return max_num(num_str) - min_num(num_str)