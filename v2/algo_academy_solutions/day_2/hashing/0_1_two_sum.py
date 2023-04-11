# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hash:
                return [i, hash[complement]]

            hash[num] = i