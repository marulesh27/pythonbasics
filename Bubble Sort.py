n=int(input())
nums=list(map(int,input().split()))
def performBubbleSort(nums):
    n= len(nums)
    for fixThisIndex in range(n - 1, 0, -1):
        
        for index in range(fixThisIndex):
         
            if nums[index] > nums[index + 1]:
                temp = nums[index]
                nums[index] = nums[index + 1]
                nums[index + 1] = temp
       

 
 
performBubbleSort(nums)
 

print(*nums)
 
