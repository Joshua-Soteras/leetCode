class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        '''
        - sum() function python
        - zero-based vs 1 based indexing 
        - Tw Pointers
        '''
        #Use Two Pointers

        #Pointer One that starts at the beginning of the array
        pOne = 0 

        #Pointer Two that starts at the end of the array
        # -1 because we want to point to the last index
        pTwo = len(numbers) - 1

        #Move pointers until on surpasses another or until we find the guaranteed solution 
        while pOne < pTwo:

        
            if (pOne+pTwo) is target:
                
                #Return the indices in one based-indexing
                pOne += 1
                pTwo += 1 
                return  [pOne, pTwo]

            elif (pOne +pTwo) > target:
                pTwo -= 1
            else:
                pOne +=1
