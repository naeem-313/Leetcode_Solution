class Solution(object):
    def reverseBits(self, n):
        b = str(bin(n)[2:])
        if(len(b)!=32):
            b=((32-len(b))*'0')+b

        
        

        c = b[::-1]
        x = int(c, 2)
        return x
        
        
        
        
        
        

       
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna