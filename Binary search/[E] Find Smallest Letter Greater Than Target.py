# Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

# Note that the letters wrap around.

# For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
 

# Example 1:

# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# Example 2:

# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
# Example 3:

# Input: letters = ["c","f","j"], target = "d"
# Output: "f"
# Example 4:

# Input: letters = ["c","f","j"], target = "g"
# Output: "j"
# Example 5:

# Input: letters = ["c","f","j"], target = "j"
# Output: "c"
 

# Constraints:

# 2 <= letters.length <= 104
# letters[i] is a lowercase English letter.
# letters is sorted in non-decreasing order.
# letters contains at least two different characters.
# target is a lowercase English letter.

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        #Binary search
        
        #Wrap around situation
        if target >= letters[-1]:
            return letters[0]
        
        # Normal binary search        
        s = 0
        e = len(letters) - 1
        
        while(s < e):
            mid = s + (e - s) // 2
            
            if letters[mid] > target:
                e = mid
            
            else:
                s = mid+1
            
        return letters[s]