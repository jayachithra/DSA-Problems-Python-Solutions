# (This problem is an interactive problem.)

# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

# You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

# MountainArray.get(k) returns the element of the array at index k (0-indexed).
# MountainArray.length() returns the length of the array.
# Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

# Example 1:

# Input: array = [1,2,3,4,5,3,1], target = 3
# Output: 2
# Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
# Example 2:

# Input: array = [0,1,2,4,2,1], target = 3
# Output: -1
# Explanation: 3 does not exist in the array, so we return -1.
 

# Constraints:

# 3 <= mountain_arr.length() <= 104
# 0 <= target <= 109
# 0 <= mountain_arr.get(index) <= 109



# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak = self.peakIndexInMountainArray(mountain_arr)
               
        res = self.binarySearch(target,mountain_arr, 0, peak, True)
        if res != -1:
            return res
        else:
            return self.binarySearch(target,mountain_arr, peak+1, mountain_arr.length()-1, False)
        
    def peakIndexInMountainArray(self, arr: 'MountainArray') -> int:
        s = 0
        e = arr.length() - 1        
        while s < e:
            mid = s + (e-s)//2            
            if arr.get(mid) < arr.get(mid+1) :
                s = mid + 1
            else: 
                e = mid                
        return e
    
    def binarySearch(self, target, arr: 'MountainArray', s, e, isIncreasing):
        while (s <= e):
            mid = s + (e-s)//2
            mid_el = arr.get(mid) #Keeping in mind the limit of calls
            if mid_el < target:
                if isIncreasing:
                    s = mid + 1
                else:
                    e = mid - 1
            elif mid_el > target:
                if isIncreasing:
                    e = mid - 1
                else:
                    s = mid + 1
            else:
                return mid
        return -1 