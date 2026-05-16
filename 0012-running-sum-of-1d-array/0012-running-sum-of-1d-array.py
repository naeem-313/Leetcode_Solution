class Solution(object):
    def runningSum(self, nums):
        sum=0
        n=[]
        
        for i in nums:
            sum+=i
            n.append(sum)
       
        return n

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna