a=[2,7,5,4,55]
target =12
#find the sum of the indeces of those numbers that will give us 12
def two_sum(nums,target):
    num_map={}
    for i,num in enumerate (nums):
        complement=target-num
    if complement in num_map:
        return[num_map[complement],i]
    else:
        num_map[num]=i