def combinationSum(candidates, target):
    result = []
    def recursion(i, current, total):
        if total == target:
            result.append(current.copy())
            return
        if i >= len(candidates) or total > target:
            return
        current.append(candidates[i])
        recursion(i, current, total + candidates[i])
        current.pop()
        recursion(i + 1, current, total)
    recursion(0, [], 0)
    return result

