'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
'''
def searchRange(nums, target):
    result = []
    left, right, i = 0, len(nums) - 1, -1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            i = mid
            right = mid - 1
    result.append(i)
    left, right, i = 0, len(nums) - 1, -1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            i = mid
            left = left + 1
    result.append(i)
    return result


