class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #The default prefix value 
        prefix = 1

        #store the results in a list
        results = [1] * len(nums)

        '''
        if nums = [1,2,3,4]
        and we want the prefix product of everything up to nums[2]
        which is 3 then..
        preifx = [1,1,2,6] 
        prefix[2] =2 since everything up to the 3rd of nums index
        would be 2

        Way to iterate backwards within an anarray 
        - range(len(nums) - 1,-1,-1)
        - num in nums[::-1]
        '''

        for index in range(len(nums)):

            #Update Results Array which will act as our prefix array
            results[index] *= prefix 
            #Update Prefix 
            prefix *= nums[index]
        

        postfix = 1
        #Traversing the Array to get Product of Array Except Self
        #Doing this Along with Post Fix Calculations
        #Start,Step,Stop
        for index in range(len(nums) - 1, -1, -1):
            results[index] *= postfix
            postfix *= nums[index]

        return results
            
            
            
        
