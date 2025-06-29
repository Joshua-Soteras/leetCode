class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #Case: If the length is 1 return 0 / Can't make profit
        if len(prices) == 1: 
            return 0
        
        #First Index
        leftPointer = 0 
    
        #2nd Index
        rightPointer = 1

        maxProfit = 0

        while rightPointer <= (len(prices) - 1):

            #If future day is lower than our current day (leftPointer)
            #Buy future day and disregard previous best day 
            if prices[leftPointer] >=  prices[rightPointer]:
                leftPointer = rightPointer

            else: 
                #Compare Profits made from current max profit 
                currentProfit = prices[rightPointer] - prices[leftPointer]
                maxProfit = max(maxProfit, currentProfit)
            
            #Move to the rightPointer to the next day 
            rightPointer += 1

        #Return 0 if negative or no profit was made
        if maxProfit <= 0 :
            return 0

        #Else: Return what was made
        return maxProfit 
