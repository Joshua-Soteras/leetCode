# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        self.diameter = 0 

        
        def dfs(node):

            if not node: 
                return 0

            #explore left side 
            radiusLeft = dfs(node.left) 
            radiusRight = dfs(node.right)  
            
            #Check if the currrent node we are at has the largest diameter
            self.diameter = max((radiusLeft+radiusRight) , self.diameter)

            radiusLeft +=1
            radiusRight +=1 
            #move up and bring the larest radius upwards (i.e. deepest path)
            return max(radiusLeft, radiusRight)

        dfs(root)
        return self.diameter 
