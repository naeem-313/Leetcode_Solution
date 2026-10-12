class Solution(object):
    def moveZeroes(self, nums):
        


        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(i)

        
        return nums
       
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna