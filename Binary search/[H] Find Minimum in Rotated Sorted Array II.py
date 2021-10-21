# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

# [4,5,6,7,0,1,4] if it was rotated 4 times.
# [0,1,4,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

# You must decrease the overall operation steps as much as possible.

 

# Example 1:

# Input: nums = [1,3,5]
# Output: 1
# Example 2:

# Input: nums = [2,2,2,0,1]
# Output: 0
 

# Constraints:

# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# nums is sorted and rotated between 1 and n times.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0
        e = len(nums) - 1
        
    
        while s < e :            
            m = s + (e-s)//2
            
            #We first try to eliminate duplicates, however, we need to make sure that we are not eliminating the minimum value
            # Hence eliminate duplicates when they are also in mid
            # For example, this will eliminate advance the start and end pointer by 1 step for this example [1, 1, 2, 1].
            # Here, by advancing one step, we are making sure that we are not eliminating 1 completely from the list           
            if nums[m] == nums[s] == nums[e]:
                s = s+1
                e = e-1
            
            # Use the same rule that we used for non-duplicate arrays
            elif nums[e] < nums[m]:
                s = m+1
            
            else: 
                e = m
                
        return nums[s]