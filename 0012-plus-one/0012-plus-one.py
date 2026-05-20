class Solution(object):
    def plusOne(self, digits):
        result = "".join(map(str, digits))
        result_int = int(result)+1

        result_s = str(result_int)
        final_result = []

        for i in range(len(result_s)):
            final_result.append(int(result_s[i]))

        return final_result





        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna