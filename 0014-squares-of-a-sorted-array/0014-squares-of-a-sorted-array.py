class Solution(object):
    def sortedSquares(self, nums):
        
        p=[]

        for i in nums:
            i*=i

            p.append(i)
        
        p.sort()
        return p


        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna