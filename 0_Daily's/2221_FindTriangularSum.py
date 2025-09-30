class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        #keep loop until only one element is left in nums
        while(len(nums) != 1):
            
            #temporary list/array to hold the next tier in the triangle
            newNums= [0] * (len(nums) - 1) 

            #Create next tier of elements/values
            for index in range(len(newNums)): 
                
                #Calculate the new number from the given formula
                newNum = (nums[index] + nums[index+1]) % 10
                
                #Assign element the new number in newNums array 
                newNums[index] = newNum
            
            #replace the array
            nums = newNums

        
        return nums[-1]
