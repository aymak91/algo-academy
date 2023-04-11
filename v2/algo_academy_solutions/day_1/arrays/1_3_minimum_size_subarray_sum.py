# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target, nums):

        left, total, res = 0, 0, float("inf")

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                res = min(right-left+1, res)
                total -= nums[left]
                left += 1
            
        return 0 if res == float("inf") else res