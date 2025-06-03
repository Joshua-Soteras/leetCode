class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #Pointer One = start of the array
        pOne = 0 

        #Pointer Two = index at the end of the array 
        pTwo = len(numbers) - 1

        #Want to keep iterating until one pointer passes the other
        #However, the solution states that there is at least one unique solution
        while pOne < pTwo: 

            #Check if our two pointers equate to the target 
            if (numbers[pOne] + numbers[pTwo]) == target:
                return [pOne + 1 , pTwo + 1]

            #Check if sum is higher than the target; If so move the pointer of the highest value down one
            #We know that the array is sorted so we move pointer two (end of array pointer)
            elif  numbers[pOne] + numbers[pTwo] > target : 
                pTwo -= 1 

            #If the sum is less than target, vice versa of the above condition 
            elif (numbers[pOne] + numbers[pTwo]) < target:
                pOne += 1
