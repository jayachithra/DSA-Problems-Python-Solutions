# Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

# Write an algorithm to minimize the largest sum among these m subarrays.

 

# Example 1:

# Input: nums = [7,2,5,10,8], m = 2
# Output: 18
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
# Example 2:

# Input: nums = [1,2,3,4,5], m = 2
# Output: 9
# Example 3:

# Input: nums = [1,4,4], m = 3
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 106
# 1 <= m <= min(50, nums.length)


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        #Binary search approach
        
        #Setting the range for binary search: The sums have a min and max range
        #Sum is minimum when the arrays are split a large number of times and vuce versa
        #Hence sum value is inversely proportional to the number of splits (m)
        #We need to find a balance between the sum and the number of splits
        e = sum(nums)
        s = max(nums)
        
        return self.binarySearch(nums, m, s, e)
        
        
    def binarySearch(self, nums, m, s, e):
        while(s < e): 
            mid = s + (e-s)//2
            counter = self.split(nums, mid)
            print(mid, counter)
            if counter > m:
                s = mid + 1
            else:
                e = mid            
        return s
            
            
    def split(self, nums, m):
        counter = 1
        tot = 0
        for i in nums:
            if i + tot <= m :
                tot += i
            else:
                tot = i
                counter += 1
        return counter
            