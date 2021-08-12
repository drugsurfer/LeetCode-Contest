def fourSum(nums: list, target: int):
    nums.sort()
    result = set()
    hashMap = {}
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            sumA = nums[i] + nums[j]
            if sumA not in hashMap.keys():
                hashMap[sumA] = []
            hashMap[sumA].append((i, j))
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            sum_ = target - (nums[i] + nums[j])
            if sum_ in hashMap.keys():
                for item in hashMap[sum_]:
                    k = item[0]
                    l = item[1]
                    if k > j:
                        result.add((nums[i], nums[j], nums[k], nums[l]))
    return [list(item) for item in result]

print(fourSum([-3,-2,-1,0,0,1,2,3],0))