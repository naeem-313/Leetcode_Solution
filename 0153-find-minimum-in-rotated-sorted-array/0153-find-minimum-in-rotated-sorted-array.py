class Solution(object):
    def findMin(self, nums):
        l = 0
        r = len(nums) - 1

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return min(nums[0], nums[1])

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
               
                l = mid + 1
            else:

                r = mid

        return nums[l]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna