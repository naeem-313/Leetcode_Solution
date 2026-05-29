class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        dict1={}

        for i in range(n):
            rem=target-nums[i]
            if rem in dict1:
                return [dict1[rem],i]
            dict1[nums[i]]=i
        
      
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna