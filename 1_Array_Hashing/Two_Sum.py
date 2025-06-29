'''
Practiced with Sanskar 
- walk through code, 
- ask for contraints and test cases 
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #target =9 
        # [2,7]
        # [0,1]

        #dicitonary to list what was seen. 
        # O(1) access time (without collisions) 
        dictionary = {}

        for index in range(len(nums)):

            complement = target - nums[index]

            if complement in dictionary: 
                return [index, dictionary[complement]]
            
            dictionary[nums[index]] = index
            
