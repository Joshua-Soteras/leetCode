class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #Pointers for usign two pointers 
        # pointerOne is the beginning of the index
        #pointerTwo points to last index
        pointerOne = 0 
        pointerTwo = len(nums) - 1

        #Mid Point of the array
        midPoint = (pointerTwo - pointerOne) // 2
        
        while pointerOne <= pointerTwo: 
            
            #if the midpoint is the target 
            if nums[midPoint] == target:
                return midPoint
            #Determing to shift the midpoint down or up within the given segment 
            elif nums[midPoint] < target:
                pointerOne = midPoint + 1 
                midPoint = (pointerTwo + pointerOne) // 2
            else:
                pointerTwo = midPoint - 1 
                midPoint = (pointerTwo + pointerOne) // 2
            
            print(pointerOne)
            print(pointerTwo)
        return -1
