class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        #list of all unique combinations that add to the target 
        res = [] 

        #subset 
        subset = []

        self.target = target

        def dfs( index, target): 
            
            #reached a unique subset that == 0 
            if target == 0: 
                res.append(subset.copy())
                return
            #negative value dont explore anymore
            elif target < 0:
                return 
            
            #target still has numbers to subtract
            elif index <len(candidates):
                
                target -= candidates[index]
                subset.append(candidates[index])
                dfs(index, target)

                #revert changes 
                target += candidates[index]
                subset.pop()
                dfs(index+1 , target)
            
            else: 
                return

        dfs(0, self.target)
        return res
