class Solution:
    def maxArea(self, height: List[int]) -> int:


        #Pointer One
        pOne = 0 

        #Pointer Two
        pTwo = len(height) - 1

        #Max Water 
        maxWater = 0 


        while pOne < pTwo:

            minHeight = min(height[pOne], height[pTwo])
            length = pTwo - pOne
            maxWater = max(maxWater, (length * minHeight))

            if (height[pOne] <= height[pTwo]):
                pOne +=1 
            else:
                pTwo -=1 


        return maxWater 

            

        
