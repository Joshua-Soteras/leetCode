class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #Pointer One = start of the array
        pOne = 0 

        #Pointer Two = index at the end of the array 
        pTwo = len(numbers) - 1

        while pOne < pTwo: 

            #Check if our two pointers equate to the target 
            if (numbers[pOne] + numbers[pTwo]) == target:
                return [pOne + 1 , pTwo + 1]

            elif  numbers[pOne] + numbers[pTwo] > target : 
                pTwo -= 1 
            
            elif (numbers[pOne] + numbers[pTwo]) < target:
                pOne += 1
