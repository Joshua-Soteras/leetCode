class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if k == len(nums):
            return nums
        #Bucket Sort
        #Create our buckets
        #Zero is the default value, index = will be frequency 
        #frequency cannot be greater than the length of the nums
        buckets = [0] * (len(nums)+1)
        answer = [0] * k


        freq = defaultdict(int)

        #Counting Frequency 
        for index in range(len(nums)): 
            
            #Update Frequncy
            #key is the actual value from numns and value is the freq
            freq[nums[index]] = freq.get(nums[index], 0) + 1
        
        print(freq)

        #Assign the keys as the values to the buckets
        maxi = 0
        for key, value in freq.items():
            
            maxi = max(maxi, value)
            if buckets[value]
            buckets[value] = key
        
        print(buckets)

        #[start: stop: step]
        for i in range(k):
            answer[i] = buckets[maxi -i]
            

        
        return answer





