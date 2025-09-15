class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.kth = k 

        #create heap
        self.minHeap = nums

        #Note: heapify in python defaults to minHeap
        heapq.heapify(self.minHeap)

        #Establish top k elements
        """
            example [1,2,3,4,5,6]
            we want the top 1 element 
            pop until we only get 1 
            [6] is returned
        """
        while len(self.minHeap) >k: 
            heapq.heappop(self.minHeap)
        


    def add(self, val: int) -> int:
        
        #if kth = 1 , minHeap = [6] , val = 2
        #minHeap = [2,6] 
        heapq.heappush(self.minHeap, val)

        #pop to maintain kth largest element property
        while len(self.minHeap) >self.kth: 
            heapq.heappop(self.minHeap)
    
        #Root node is the kth largest element 
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
