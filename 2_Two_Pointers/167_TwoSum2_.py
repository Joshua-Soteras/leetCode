class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        #mention this first before code 
        #space complexity : O(1)
        #time complexity: O(n)

        left = 0 
        right = len(numbers) -1 


        while left < right: 
            
            twoSum = numbers[left] + numbers[right]

            if (twoSum) == target: 
                return [left + 1 , right + 1]

            elif twoSum < target:
                left +=1 

            else : right -=1

        
