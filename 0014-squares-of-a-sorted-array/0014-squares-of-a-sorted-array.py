class Solution(object):
    def sortedSquares(self, nums):
        
        d=[]

        for i in nums:
            d.append(i*i)
        

        return sorted(d)

        
        
       


        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna