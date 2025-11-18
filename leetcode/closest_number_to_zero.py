# given integer array nums of size n
# return the number with the closest value to zero
# if there are multiple answers return the higher value

def closerToZero(nums):
    a = (abs(nums[1]),nums[1])
    for num in nums:
        b = abs(num)
        if b<a[0]:
            a = (b,num)
        elif b==a[0] and num!=a[1]:
            a = (b,b)
    return a[1]

print(closerToZero([5,2,-2,1,3,4,-1]))
