class Solution(object):
    def thirdMax(self, nums):
        num = set(nums)
        num1=list(num)
        n=len(num1)

        

        if n<3:
            return max(num1)

        num1.remove(max(num1))
        num1.remove(max(num1))

        return max(num1)


       
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna