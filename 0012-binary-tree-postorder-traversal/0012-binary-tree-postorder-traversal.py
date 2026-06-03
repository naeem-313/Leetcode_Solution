# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        def __init__ (self):
            self.ans=[]
    
    def postOrder(self,root):
        if root is None:
            return

        self.postOrder(root.left)
        self.postOrder(root.right)
        self.ans.append(root.val)
    def postorderTraversal(self, root):
       
        self.ans=[]
        self.postOrder(root)
        
        
        return self.ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna