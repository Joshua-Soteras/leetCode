#### HEAPPUSHPOP
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #given a list of list ints
        #each index within the list contains an x and y coordinate 
        #at least one point within points is given
        #x any y values will always exists 
        
        #list / heap 
        distances = []

        #calculate distances from origin:
        #go through each of the points within the given list points 
        for x,y in points: 
            
            #calculate Euclidean distance
            distance = (math.sqrt( (x-0 )**2 + (y -0)**2 ))

            #push calculated distances and points onto the heap
            #values are stored in a tuple and sorted based on distance (first value of tuple)
            heapq.heappush(distances , (distance , [x,y]) )
        
        res = []
        
        for i in range(k): 

            closestPoints = heapq.heappop(distances)
            res.append(closestPoints[1])

        return res






            


