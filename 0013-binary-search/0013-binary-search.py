class Solution(object):
    def search(self, nums, target):
        n=len(nums)
        low=0
        high=n-1
       

        for i in range(n):
            mid =(low+high)//2
            if nums[mid] ==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1

        return -1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna