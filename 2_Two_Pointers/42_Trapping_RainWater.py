class Solution:
    def trap(self, height: List[int]) -> int:

        #left and right pointers to keep moving 
        leftPointer = 0
        rightPointer = len(height) - 1 

        #keep track of container sides
        #the largest we've seen on the left
        #the largerst we've seen on the right
        maxLeft, maxRight  = height[leftPointer],\
        height[rightPointer]

        #no water by default
        water = 0 

        while(leftPointer < rightPointer):
            
            #calculate based on the smallest side
            if maxLeft < maxRight: 
                
                #move pointer 
                leftPointer +=1
                
                #compare new position to max left side
                #if the new position is larger then update
                maxLeft = max(height[leftPointer] , maxLeft)

                #add water (if any)
                water += maxLeft - height[leftPointer]

            #we know the largest side we've is then right
            else:

                #move pointer 
                rightPointer -=1
                
                #compare new position to max left side
                #if the new position is larger then update
                maxRight = max(height[rightPointer] , maxRight)

                #Add water (if any)
                water += maxRight - height[rightPointer]

        return water
