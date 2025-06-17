class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        #from collections import deque
        stack = deque()
        segment = 0
        tempLength = 0

        #index, height
        minHeight = None
        maxArea = 0 

        for index, height in enumerate(heights):
            
            if height == 0:
                minHeight = None
                segment = 0

            if (minHeight == None or minHeight > height) and height != 0 :
                minHeight = height
                print("Current Min Height" , height)

            if not stack:
                stack.append(height)
                maxArea = height
        
            elif stack[-1] > height:
                
                #calculate the area to everything of the left 
                # + 1 to account for current height 
                width = len(stack) + 1
                tempStack = 
                maxArea = max( maxArea, (height * width))

                #calculate each possilbe area of the hieghts in the stack
                while stack: 
                    maxArea = max(maxArea, (stack[0] * len(stack)))
                    stack.popleft()

                stack.append(height)
            
            #Continue the stack since current height is dependent on the previous height
            else: 
                maxArea = max( maxArea, height)
                stack.append(height)
            
            if height != 0:
                segment += 1
                print("SEGEMENT:" , segment* minHeight)
                maxArea = max (maxArea, segment* minHeight)
        
        while stack: 
                maxArea = max(maxArea, (stack[0] * len(stack)))
                stack.popleft()
    

        return maxArea





