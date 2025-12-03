class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        """ 

        Step 1 Analyze : 

        - what is being returned? 
            - returning a 2D list where water can flow 
            - return a list of valid coordinates
            - just valid coordinates where water can flow 
            - size of matrix 
        - given a 2d matrix of ints 
        - each element represents  a height 
        - there has to be at least 1 element in the 2D matrix 

        Step 2 Psuedo code
            - thinking o two sets 
            - set 1: from pacific to atlantic 
            - set 2 : from atlantic to paficic
            - take union between these two sets to return valid flows
            - have to go through each cell a
            - Time Complexity: O(m*n)
            - Note V = m*n where V is vertices 
            - Space Comple
        """ 

        pOcean = set()
        aOcean = set()
    


        rows = len(heights)
        cols = len(heights[0])
        
        #looks in four directions = down, up , right, left
        directions = [(1,0), (-1,0) , (0,1) , (0,-1)]

        #r and c are current values of row and index
        def dfs(r: int, c:int , ocean: set): 
            
            ocean.add((r,c))
            #traverse each direction
            for dirR , dirC in directions: 
                
                #exploring next element
                row , col = r + dirR , c + dirC

                #skip: 
                #if out of boundaries
                #if already visited
                if row < 0 or row >= rows\
                or col < 0 or col >= cols\
                or (row,col) in ocean: 
                    continue 
                
                #add to visited 
            
                if heights[row][col] >= heights[r][c]:
                   
                    dfs(row,col, ocean)

            #if all routes have been traversed then we are at peak

            


        for c in range(cols): 
            dfs(0, c, pOcean)

        for r in range(rows):
            dfs(r , 0, pOcean)

        
        for c in range(cols-1,-1,-1 ): 
            dfs(rows-1, c, aOcean)

        for r in range(rows-1,-1,-1):
            dfs(r, cols-1, aOcean)

        peaks=[]
        for r in range(rows): 
            for c in range(cols):

                if (r,c) in pOcean\
                and (r,c) in aOcean:
                    peaks.append([r,c])

        return peaks
