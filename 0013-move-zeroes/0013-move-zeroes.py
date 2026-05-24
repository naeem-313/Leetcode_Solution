class Solution(object):
    def moveZeroes(self, nums):
        count=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[count],nums[i]=nums[i],nums[count]
                count+=1

        return nums
       
        
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna