# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        '''
          Note: good nodes are considered valid if there no values bigger than our current value to the root (including root)
        '''
        #counter for goodNodes
        self.counter = 0

        #Recursive dfs
        def dfs(node , maxVal): 
            
            if not node:
                return 
            
            if node.val >= maxVal:
                self.counter +=1
            
            dfs(node.left, max(maxVal, node.val))
            dfs(node.right, max(maxVal, node.val))


        dfs(root, root.val)
        return self.counter

