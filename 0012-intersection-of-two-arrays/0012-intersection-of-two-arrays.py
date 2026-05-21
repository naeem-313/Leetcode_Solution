class Solution(object):
    def intersection(self, nums1, nums2):
        seen=set(nums1)

        res=[]

        for n in nums2:
            if n in seen:
                res.append(n)
                seen.remove(n)


        return res

                

       
      

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna