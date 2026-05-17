class Solution(object):
    def getSum(self, a, b):
        mask=0xFFFFFFFF
        while b&mask>0:
            temp=(a&b)<<1
            a=a^b
            b=temp

        return (a&mask) if b>0 else a
       


       
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna