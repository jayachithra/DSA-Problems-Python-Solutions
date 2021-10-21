# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
 

# Constraints:

# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Koko can eat a minimum of 1 bananas and maximum of max number of bananas in the list per hour
        #This will be the start and end of our search space i.e., the answer should lie between these values
        start = 1
        end = max(piles)
        
        #If there is only one pile, then divide the pile equally per hour
        if len(piles) == 1:
            return ceil(piles[0]/h)
        
        return self.binarySearch(piles, h, start, end)
                        
        
    def binarySearch(self, piles: List[int], h: int, start: int, end: int) -> int:
        while (start < end):
            mid = start + (end - start)//2
            if self.isPossibleAnswer(piles, mid) <= h: #This is a possible answer . The answer should lie here or below it.
                end = mid
            else:
                start = mid + 1            
        return start        
                                
            
    def isPossibleAnswer(self, piles: List[int], mid: int):
        hourCount = 0
        
        #Iterate per item in list -> list is smaller than iterating per hour
        for i in piles:
            #i can be less than, equal to or greater than mid
            hourCount += 1 if i<= mid else ceil(i/mid) 
        
        return hourCount
                
        
        
        
#         #For each hour consume mid number of bananas (or less depending on the bucket)
#         #In the end of h hours, check if all the bananas are consumed
#         for i in range(h): 
#             if pilePointer > len(piles)-1:
#                 break
#             if piles[pilePointer] > mid:
#                 piles[pilePointer] -= mid
#             else:
#                 piles[pilePointer] = 0                
#                 #What if all the items are cosumed before the hour?                 
#                 pilePointer += 1
#             hourCount += 1
        
#         #End of the hour, check if all the bananas are eaten
#         return False if sum(piles)>0 else True
            
            
            
            
        
        