# https://leetcode.com/problems/arranging-coins/

# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

 

# Example 1:


# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.
# Example 2:


# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
 

# Constraints:

# 1 <= n <= 231 - 1

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # min number of rows we can have is 1 & max is 
        s, e = 1, n
        
        #Each row number can have a maximum for n(n+1)/2 coins
        while (s <= e):
            m = s + (e-s)//2  
            if ((m)*(m+1))/2 == n:
                return m
            if ((m)*(m+1))/2 < n: # m rows can't contain all the data, Increase the rows
                s = m+1
                
            else: e = m-1
        
        return e
        
      