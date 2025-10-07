class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        twoLargestStones = 2 

        #edge case if there is only one stone
        if len(stones) <= 1: 
            return stones[-1]

        #heapify the given list (stones and their weights)
        #note in python, heapify makes a min heap by default
        #we need to make max heap by negating 
        maxHeap = [-stone for stone in stones]
        
        #Heapify new list
        heapq.heapify(maxHeap)

        #continuing poping two largest stones
        while len(maxHeap) > 1:

            #Revert the negation and get the largest stone
            y = -(heapq.heappop(maxHeap))
            x = -(heapq.heappop(maxHeap))

            if x!=y: 
                #take absolute value of the stones mashed together (remaing weight)
                newStone = -(y-x)
                heapq.heappush(maxHeap, newStone)
        
        
        return 0 if len(maxHeap) == 0 else -(maxHeap[0])



        
            
