class Solution(object):
    def firstUniqChar(self, s):
        freg={}
        for i in s:
            if i not in freg:
                freg[i]=1
            else:
                freg[i]+=1

        for i in range(len(s)):
            if freg[s[i]]==1:
                return i

        return -1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna