# A peak element is an element that is strictly greater than its neighbors.

# Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

# Constraints:

# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        s = 0
        e = len(nums)-1
        
        while (s <= e):
            m = s + (e-s)//2
            
            # First check: Is m the peak element? This is possible if m is greater than it's neighbours
            # Edge case : If m is a corner element, then you only have to check one neighbour. 
            # Make sure you don't get index out of bounds error in this case
            if (m+1 >= len(nums) or nums[m] > nums[m+1]) and (m-1 < 0 or nums[m] > nums[m-1]):
                return m
            
            #Second : if m is not peak, check if it is in increasing slope
            # make sure m+1 is not out of bounds
            if (m+1 < len(nums)) and (nums[m] < nums[m+1]):
                s = m + 1
            elif (m-1 >= 0) and (nums[m] < nums[m - 1]): # m is in decreasing slope, move search space to left
                e = m - 1
                
        return -1
            