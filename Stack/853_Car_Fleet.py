class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        '''
            Timsort = merge() 
            zip()
            tuples
            accessing tuples values 
            .sort 

            cars = [(10, 2), (8, 4), (0, 1), (5, 1), (3, 3)]

            # Sort by first element (position)
            cars.sort(key=lambda x: x[0])  # ascending by position

            # Sort by first element descending
            cars.sort(key=lambda x: x[0], reverse=True)

            tuples 
            More general form:
            lambda arguments: expression
            It's a small function without a name that returns the result of the expression.
        '''

        #calculate times of arrival. 
        #pos = 10 and speed = 2 then time of arrival is at 1 for target 12

        positionAndSpeed= list(zip(position, speed))

        #time complexity is nlgn
        #sort the times reach in 
        positionAndSpeed.sort(key=lambda x:x[0], reverse=True)

        #storing time it took to reach target
        times = []

        #stack to find carfleet
        stack = deque()
        for item in positionAndSpeed: 
            
            #Calculate time to reach target
            #Time Distance Speed Formula 
            time = (target - item[0]) / item[1]
            
            #Append Time
            times.append(time)

        for index in range(len(times)):
            
            if (not stack) or (stack[-1] < times[index]):
                stack.append(times[index])
            

        return len(stack)
         
