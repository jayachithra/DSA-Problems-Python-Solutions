# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return self.searchInRotatedArray(nums, target)
        
        pivot = self.findPivotPoint(nums)
        
        if pivot == -1: #no pivot
            return self.binarySearch(nums, 0, len(nums)-1, target) #normal binary search
        
        if nums[pivot] == target: #pivot is the target
            return pivot
        
        #there is a pivot
        if target >= nums[0]:
            #Search space is halved
            return self.binarySearch(nums, 0, pivot-1, target)
        else:
            return self.binarySearch(nums, pivot+1, len(nums)-1, target)
    
    
    def binarySearch(self, nums, s, e, target):
        while (s <= e):
            mid = s + (e-s)//2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                e = mid - 1
            else:
                s = mid + 1
        return -1    
    
    
    def findPivotPoint(self, nums):
        s = 0
        e = len(nums) - 1
        while s <= e:
            m = s + (e-s)//2
            if (m < e) and (nums[m] > nums[m+1]): #M is the pivot index
                return m
            if (m > s) and (nums[m-1] > nums[m]): #m-1 is the pivot
                return m-1
            if nums[m] < nums[s]: #Ascending order
                e = m - 1
            else:
                s = m + 1
        return -1