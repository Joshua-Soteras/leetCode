# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        self.flag = True

        #post -> left, right , node
        def dfs(node):
        
            if not (node.left or node.right):
                return 1
        
            left = dfs(node.left) +1 if node.left else 1
            right = dfs(node.right) + 1 if node.right else 1
            
            largest = max(left, right)
            smallest = min(left,right)
    

            if (largest-smallest) > 1:
                self.flag = False

            return largest
            #compare depths s



        dfs(root) if root else None
        return self.flag


    
        
