class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #use binary search to search whole array 
        '''
            - intution: 
            search for target value and we know each row is sorted
                - use binary search: Time complexity O(lgn )
                - if the right pointer is less than target -> next row
                - other wise perform binary search 
                - constraint: lg(m*n)
                - column is outer binary and row is inner binary search

        '''

        #pointer to top of maxtrix col
        topPointer = 0 
        
        #get len of col to pointer to bottom of matrix col
    
        bottomPointer = len(matrix) -  1 
        print(bottomPointer, "length")

        #outer binar search is for 
        while(topPointer <= bottomPointer): 
            
            #leftPointer is the midPointer for the col but left for row
            midColPoint = (bottomPointer + topPointer) // 2 
            print(matrix[midColPoint][0])
            if matrix[midColPoint][0] == target:
                return True

            if matrix[midColPoint][0] < target:
                
                #current row length to point to last element of row
                leftPointer = 0
                rightPointer = (len(matrix[midColPoint]) -1 )

                while (leftPointer <= rightPointer):
                    
                    #update mid point 
                    midRowPointer = (leftPointer + rightPointer) // 2 

                    #found target return true
                    if matrix[midColPoint][midRowPointer] == target:

                        return True
                    
                    #increment/decrement for left/right Pointer
                    elif matrix[midColPoint][midRowPointer] < target:
                        leftPointer = midRowPointer + 1

                    else:
                        rightPointer = midRowPointer - 1
                
                #didn't find in this row so decrement bottom pointer
                #might be in a row less than the current one we are at
                #move it midpoint of col -1
                topPointer = ((bottomPointer + topPointer) // 2) + 1
            
            else:
                #move topPointer to midpoint of col + 1
                bottomPointer = ((bottomPointer + topPointer) // 2) - 1

        return False


            
            


    

