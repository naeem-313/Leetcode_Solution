class Solution(object):
    def findDisappearedNumbers(self, nums):
       
        n=len(nums)
        nums=set(nums)
        missing=[]
        
        


        for i in range(1,n+1):
            if i not in nums:
                missing.append(i)


        return missing
       
            
            

       
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna