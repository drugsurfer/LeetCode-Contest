'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
'''
def threeSumClosest(nums : list, target : int):
    result = sum(nums[:3])
    nums.sort()
    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = nums[i] + nums[l] + nums[r]
            if abs(threeSum - target) < abs(result - target):
                result = threeSum
            if threeSum < target:
                l += 1
            else:
                r -= 1
    return result
