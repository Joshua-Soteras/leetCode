class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        """ 
            Thoughts: 

            -   when rotated the min is usually pushed to the right side

            -   left and midpoint have to be less in
                the right pointer to be in acsending order
        """
        minNum = nums[0]

        #left pointerr to first index 
        left = 0 

        #right pointer to last value of the index
        right = len(nums)-1

        while(left <= right):

            mid = (left + right) // 2 

            minNum = min(minNum , nums[mid]) 

            #in greater part o, )f the subarray
            if nums[mid] > nums[right]: 

                left = mid + 1
            else: 

                right = mid - 1

        
        return minNum 
