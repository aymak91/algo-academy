# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height):
        max_water, left, right = 0, 0, len(height)-1

        while left < right:
            shorter = min(height[right], height[left])
            area = (right-left) * shorter

            if area > max_water: max_water = area

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1

        return max_water