# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Follow up: Do not use any built-in library function such as sqrt.

 

# Example 1:

# Input: num = 16
# Output: true
# Example 2:

# Input: num = 14
# Output: false
 

# Constraints:

# 1 <= num <= 2^31 - 1

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #Basic solution - Iterate all the previous numbers until a threshold is reached
        # start = 1
        # while True:
        #     if (num/start == start):
        #         return True
        #     elif ceil(num/start) < start:
        #         return False
        #     start += 1
        
        # Binary search
        if num == 1:
            return True
        
        start = 1
        end = num//2
        
        while (start <= end):
            mid = start + (end - start)//2            
            if mid*mid == num:
                return True
            elif mid*mid < num:
                start = mid + 1
            else:
                end = mid - 1
                
        return False