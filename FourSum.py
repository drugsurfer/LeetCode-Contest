def fourSum(nums: list, target: int):
    result = []
    nums.sort()
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums)):
            l, r = j + 1, len(nums) - 1
            while l < r:
                sum4 = nums[i] + nums[j] + nums[l] + nums[r]
                if sum4 == target:
                    if [nums[i], nums[j], nums[l], nums[r]] not in result:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                    r -= 1
                elif sum4 > target:
                    r -= 1
                else:
                    l += 1
    return result
