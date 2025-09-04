class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh = 0 
        time = 0
        q = deque()


        for row in range(len(grid)):
            for col in range(len(grid[0])):

                #increment total of oranges found
                if grid[row][col] == 1:
                    fresh +=1
                
                #Keep track of rotting oranges
                #store in queue for BFS
                elif grid[row][col] == 2:
                    q.append((row,col))

        #Directions to look for fresh oranges
        #up, right, down,left
        directions = [[-1,0] , [0,1], [1,0], [0,-1]]

        #while the q is not empty
        while q and fresh: 
            
            #Each q and what it contains is the current time /state of rotting
            for i in range(len(q)):
                rowRot, colRot= q.popleft()
                for dirRow, dirCol in directions:
                    row , col = rowRot + dirRow , colRot + dirCol

                    #if out of bounds or not a fresh orange continue to next iteration
                    if( row < 0 or col < 0 or  
                        row >=len(grid) or col >= len(grid[0]) or
                        grid[row][col] != 1):
                        continue
                    
                    #change fresh orange to rotten
                    grid[row][col] = 2
                    #add new rotten orange to q 
                    q.append((row,col))
                    #1 less fresh orange if infected
                    fresh -=1 
 
            time +=1

        return time if fresh == 0 else  -1
        
