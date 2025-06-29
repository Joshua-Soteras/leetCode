class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        '''
            import math 
            ciel
            You can use -(-pile // k) in Python to do ceiling division without importing math. 
        ''' 
        #Using Binary Search to Minimum Rate

        #Min Rate is 1 fucking Banana an hour
        leftPointer = 1

        #Max Rate is the largest pile of bananas
        rightPointer= max(piles)
        
        #Rate (default to the midpoint)
        rate = math.ceil( (rightPointer + leftPointer) / 2 )

        #Minimum Rate
        minRate = rightPointer

        #Find the minimum eating rate k pile 
        while leftPointer <= rightPointer:
            
            eatingTime = 0 

            #midPoint is the current eating rate we are look at
            for b in piles: 

                #We take the cieling of the division 
                #I.E. Koko won't do anything if she finishes eating and the hour is finished yet
                eatingTime += math.ceil( b / rate )

            print(eatingTime)
            
            #Adjust Pointers and see if we can find a lower rate
            if eatingTime <= h: 

                #Compare and take min rate
                minRate = min(minRate, rate)

                rightPointer = rate - 1
                rate = (rightPointer + leftPointer) // 2

            
            #Move the pointers up / need faster rate
            else:
                leftPointer = rate + 1
                rate = (rightPointer + leftPointer) // 2

        return minRate
