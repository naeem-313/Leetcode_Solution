class Solution(object):
    def missingNumber(self, nums):
        nums.sort()

        for i in range(len(nums)):
            if i!=nums[i]:
                return i

        if len(nums) not in nums:
            return len(nums)


        
        