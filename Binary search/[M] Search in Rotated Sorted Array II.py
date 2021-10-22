# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.

 

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
 

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# nums is guaranteed to be rotated at some pivot.
# -104 <= target <= 104


class Solution:
    def search(self, nums: List[int], target: int) -> bool:        
        s = 0
        e = len(nums) - 1        
        
        while(s <= e):
            m = s + (e-s)//2
            
            # If the target element is start or mid or end element, return True
            if (target == nums[m] or target == nums[s] or target == nums[e]):
                return True
            
            # If start, end and mid are all the same element, move start and mid by 1 place
            if (nums[m] == nums[s] == nums[e]):
                s = s+1
                e = e-1
            
            # The first half is ordered
            elif nums[s] <= nums[m]:
                if nums[s] < target < nums[m]:
                    e = m - 1
                else:
                    s = m + 1
                    
            # The second half is ordered
            else:
                if nums[m] < target < nums[e]:
                    s = m + 1
                else:
                    e = m - 1
            
        return False