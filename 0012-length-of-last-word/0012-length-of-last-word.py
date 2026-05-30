class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()
        
        n=len(s)

        i=-1
        while i>=(-1*n) and s[i]!=" ":
            i-=1

        i+=1
        i*=-1

        return i
       
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna