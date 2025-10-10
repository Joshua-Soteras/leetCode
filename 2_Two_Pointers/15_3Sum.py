class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        nums.sort()
        #append results of 3sum combinations here
        res = []
            
        #boundary 
        #len(nums) -2 because we know k is at len(nums)-1
        for i in range(len(nums) - 2 ):
            
            #check for reapeating values of if nums[i]
            #[-1 -1, 0, 2 ]
            if  i > 0 and nums[i] == nums[i-1]:
                continue

            #reset left and right pointers
            j = i + 1
            k = len(nums) -1 
            
            while j < k: 
                
                total = nums[i] + nums[j] + nums[k]
                if total == 0 :

                    res.append( [nums[i], nums[j], nums[k]] )

                    #found a 3 sum, increment j and left from where they are
                    #do not want duplicate values
                    while  j<k  and nums[j] == nums[j+1]: 
                        #[-1,-1,-1,-1,0]
                        j += 1  

                    while j<k and nums[k] == nums[k-1]:
                        k -= 1  
                    
                    j += 1
                    k -= 1

                #if the total is greater than 0 move right pointer down
                elif total > 0:
                        k -= 1 

                else: 
                        j += 1  
                        
        return res




