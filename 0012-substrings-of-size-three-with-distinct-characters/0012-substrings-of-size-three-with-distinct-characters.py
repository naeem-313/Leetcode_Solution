class Solution(object):
    def countGoodSubstrings(self, s):
        n=len(s)

        ans=0

        for i in range(n-2):
            if s[i]!=s[i+1] and s[i+1]!=s[i+2] and s[i+2]!=s[i]:
                ans+=1

        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna