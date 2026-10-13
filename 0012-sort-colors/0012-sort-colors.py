class Solution(object):
    def sortColors(self, nums):

        counts=[0,0,0]

        for color in nums:
            counts[color]+=1


        r,w,b=counts
        nums[:r]=[0]*r
        nums[r:r+w]=[1]*w
        nums[r+w:]=[2]*b
       
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna