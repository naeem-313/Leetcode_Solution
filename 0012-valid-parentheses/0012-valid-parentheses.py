class Solution(object):
    def isValid(self, s):
        n=len(s)
        if n%2==1:
            return False

        
        st=[]
        for ch in list(s):
            if ch=='(' or ch=='{' or ch=='[':
                st.append(ch)
            else:
                if len(st)==0:
                    return False
                
                top=st.pop()

                if ch==')' and top!='(':
                    return False
                elif ch=='}' and top!='{':
                    return False
                elif ch==']' and top!='[':
                    return False

        
        return len(st)==0
       
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna