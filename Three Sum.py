def threeSum(nums : list):
    result = []
    nums.sort()
    for i, value in enumerate(nums):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = value + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                result.append([value, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1]:
                    l += 1
    return result


print(threeSum([-1,0,1,2,-1,-4]))