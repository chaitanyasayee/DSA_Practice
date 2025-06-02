class Solution:
    def candy(self, ratings: List[int]) -> int:
        arr = [1] * len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i-1] < ratings[i]:
                arr[i] = arr[i-1] +1
        for b in range(len(ratings)-2,-1,-1):
            if ratings[b] > ratings[b +1]:
                arr[b] = max(arr[b],arr[b+1] +1)
        return sum(arr)