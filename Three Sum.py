def threeSum(nums : list):
    # [-1,0,1,2,-1,-4]
    '''
    
    '''
    result = []
    hashMapThree = {}
    for i, x in enumerate(nums):
        target = -x
        # twoSum
        hashMapTwo, temp = {}, []
        for j, n in enumerate(nums[i + 1:]):
            diff = target - n
            if diff in hashMapTwo:
                temp.append([nums[i + 1:][hashMapTwo[diff]], nums[i + 1:][j]])
            hashMapTwo[n] = j
        if len(temp) != 0:
            for sum_ in temp:
                if sorted([x] + sum_) not in result:
                    result.append(sorted([x] + sum_))
    return result

print(threeSum([0]))