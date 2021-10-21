# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

class Solution(object):  
    def searchRange(self, nums: List[int], target: int) -> List[int]:        
        arr = [-1, -1]    
        arr[0] = self.binarySearch(target, nums, isStart = True)
        if arr[0] != -1:
            arr[1] = self.binarySearch(target, nums,isStart = False)
        return arr
    
    def binarySearch(self, target, nums, isStart):
            s = 0
            e = len(nums) - 1
            idx = -1             
            while s <= e:
                mid = s + (e-s)//2
                if nums[mid] < target:
                    s = mid + 1
                elif nums[mid] > target:
                    e = mid - 1
                else:
                    idx = mid
                    if isStart:
                        e = mid-1
                    else:
                        s = mid+1
            return idx
        