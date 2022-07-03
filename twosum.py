# my solution

# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i != j and nums[i]+nums[j] == target:
#                 return [i,j]
# print(twoSum([2,7,11,15],9))

#their solution
# learn enumerate
def twoSum(nums,target):
    prevMap = {} # val -> index
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

print(twoSum([2,7,11,15],9))
