# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

 

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        s = 0 
        e = len(nums) - 1
        
        while (s<e):
            m = s + (e-s)//2
            
            # METHOD 1
            
#             if (nums[m-1] < nums[m] < nums[m+1]):
#                 return nums[m]
            
#             # Series not broken before mid
#             if ((m%2 == 0) and (nums[m] == nums[m+1])) or ((m%2 == 1) and (nums[m-1] == nums[m])):
#                 s = m+1
#             else:
#                 e = m
                
            # METHOD 2 
            # Case 1: When m is not a duplicate
            if ((m-1)>=0) and  (m+1 < len(nums)) and (nums[m-1] < nums[m] < nums[m+1]):
                return nums[m]
            
            # Case 2: When m is the first of it's duplicate
            if nums[m] == nums[m+1]: # m is the first copy of the number
                if (m - s)%2 != 0: # Odd number elements before m
                    e = m-1
                else:
                    s = m
            # Case 3: When m is the second of it's duplicate
            else :
                if (e - m)%2 != 0: # Odd number of elements after m
                    s = m+1
                else:
                    e = m
        return nums[s]
                
        