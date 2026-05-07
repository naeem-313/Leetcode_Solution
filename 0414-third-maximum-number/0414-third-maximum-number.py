class Solution(object):
    def thirdMax(self, nums):
        num = set(nums)
        num1 = list(num)

        if len(num1)<3:
            return max(num1)

        num1.remove(max(num1))
        num1.remove(max(num1))

        return max(num1)
        

       


   
        
         
        