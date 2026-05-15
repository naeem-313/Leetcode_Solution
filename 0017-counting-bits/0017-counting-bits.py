class Solution(object):
    def countBits(self, n):
        b = 0
        c = []
        for i in range(0, n+1):

            b = (bin(i)[2:]).count('1')
            c.append(b)

        return c
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna