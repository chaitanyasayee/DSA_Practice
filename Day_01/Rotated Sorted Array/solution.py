def search(nums: list[int]) -> int:
    if not nums: 
        return -1  

    l = 0
    r = len(nums) - 1  

    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:  
            l = mid + 1 
        else:
            r = mid  
    
    return l  

t = int(input())

while t > 0:
    num = int(input())

    nums = list(map(int, input().split()))

   
    if len(nums) != num:
        print("Error: Expected", num, "elements but got", len(nums))
    else:
        print(search(nums))  

    t -= 1 
