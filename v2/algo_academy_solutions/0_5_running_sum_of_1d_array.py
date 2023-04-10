class Solution:
    def runningSum(self, nums):
        
        prefixSum = [nums[0]]
        
        for i in range(1, len(nums)):
            prev = prefixSum[-1]
            prefixSum.append(prev+nums[i])
            
        return prefixSum