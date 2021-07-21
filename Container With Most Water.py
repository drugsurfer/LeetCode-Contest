'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
'''
def maxArea(height : list):
    maxH = 0
    i, j = 0, len(height) - 1
    while i < j:
        s = (j - i) * min(height[i], height[j])
        if s > maxH:
            maxH = s
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
    return maxH

print(maxArea([1,8,6,2,5,4,8,3,7]))
