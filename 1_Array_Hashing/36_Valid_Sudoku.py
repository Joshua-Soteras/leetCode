class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        """
            Condition 1: no two or more same values in the same row
            Condition 2: no tow or more same values in the same col
            Condition 3: no two or more same values in the same section
        """

        #Dictionary (empty)
        # keep track of values encountered and sections visited 
        values = {}


        #Dictionary (empty) : will show case the value and where they exist
        rows = {}
        cols = {}
        
        #Steps and process 
        # 1. check if the value exist within a row  
        # 2. check if the value exist with a colum,
    
        #Looping through rows 
        for rIndex in range(len(board)):

            #Loopings through columns 
            for cIndex in  range(len(board)):
                
                if board[rIndex][cIndex] != '.': 
                    #if the value on the board has been encountered already
                    if board[rIndex][cIndex] in values: 
                        
                        #Condtion 3: check if there has been any duplicates in the same section
                        section = (rIndex // 3) * 3 + (cIndex // 3)
                        #If the value is already associated with a section return false
                        if section in values[board[rIndex][cIndex]]: 
                            return False
                        #else add to new section to the associated value 
                        else: 
                            values[board[rIndex][cIndex]].add(section)

                        #Condition 1 and 2: Check: if there is a same value in the row or col
                        if (rIndex in rows[board[rIndex][cIndex]]) or (cIndex in cols[board[rIndex][cIndex]]):
                            return False
                        else: 
                            rows[board[rIndex][cIndex]].add(rIndex)
                            cols[board[rIndex][cIndex]].add(cIndex)
                        

                    #Not been encountered: add to the list of values r
                    else: 

                        #Adding new value + section 
                        section = (rIndex // 3) * 3 + (cIndex // 3) 
                        values[board[rIndex][cIndex]] = {section}

                        #Dictionary of values with associated rows 
                        rows[board[rIndex][cIndex]] = {rIndex}
                        cols[board[rIndex][cIndex]] = {cIndex}
                    
                    
        return True 
               

            



        
