class Solution(object):
    def missingNumber(self, nums):
        nums.sort()

        for i in range(len(nums)):
            if i!=nums[i]:
                return i

        if len(nums) not in nums:
            return len(nums)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna