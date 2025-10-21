class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


        #store the results of the subsets in this list
        res = [] 

        subset = []


        def dfs(i:int): 

            #base case 
            #exhausted all options 
            #append the subset to the result
            if i >= len(nums): 
                #need to copy because ultimately we will pop off while exploring right side
                res.append(subset.copy())
                return 

            #left side of the tree: add to subset
            subset.append(nums[i])
            dfs(i+1)

            #right side of substree: nothing
            #pop to revert the change we made 
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res 
        
