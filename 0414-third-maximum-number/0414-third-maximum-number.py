class Solution(object):
    def thirdMax(self, nums):
        num = set(nums)
        num1=list(num)
        n=len(num1)

        if n<3:
            return max(num1)

        num1.remove(max(num1))
        num1.remove(max(num1))


        return max(num1)
       

       


   
        
         
        