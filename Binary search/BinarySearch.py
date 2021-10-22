# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 22:31:15 2021

@author: jaya.kumar
"""

class BinarySearch:
    
    # def __init__(self, order):
    #     self.order = order
      
    
    """
    Method to get the index of a target element in a (inreasingly) sorted array using binary search O(log n)
    
    Parameters
    ----------
    nums : List of ints => sorted array
    target : int => target value to find in array
    
    Output
    --------
    index of element : int => returns the index of the target in the array. Return -1 if target is not found
    
    """   
    def get_index_asc_array(self, nums, target):
        s = 0
        e = len(nums)-1
        while s <= e:
            m = s + (e-s)//2
            
            # IF target element is mid return index
            if nums[m] == target:
                return m
            # Case when target element is on the left half
            elif nums[m] < target:
                s = m + 1
            # Case when target element is on the right half
            else:
                e = m - 1
        return -1
    
    
    """
    Method to get the index of a target element in a sorted array (ascending or descending) using binary search O(log n)
    
    Parameters
    ----------
    nums : List of ints => sorted array
    target : int => target value to find in array
    
    Output
    --------
    index of element : int => returns the index of the target in the array. Return -1 if target is not found
    
    """   
    def get_index(self, nums, target):
        
        s = 0
        e = len(nums)-1
        
        # Find if it is sorted ascending or descending
        if nums[s] < nums[e]:
            is_asc = True
        else:
            is_asc = False
        
        while s <= e:
            m = s + (e-s)//2
            # IF target element is mid return index
            if nums[m] == target:
                return m
            
            # IF the array is ascending
            if is_asc:            
                # Case when target element is on the left half
                if nums[m] < target:
                    s = m + 1
                # Case when target element is on the right half
                else:
                    e = m - 1
            
            # If the array is desending
            else:            
                # Case when target element is on the left half
                if nums[m] > target:
                    s = m + 1
                # Case when target element is on the right half
                else:
                    e = m - 1
        return -1
    
    
if __name__ == "__main__":
    bs = BinarySearch()
    print(bs.get_index_asc_array([0,1,2,3,4], 1))
    print(bs.get_index_asc_array([1], 1))
    print(bs.get_index_asc_array([0,1,2,3,4], 5))
    print(bs.get_index_asc_array([0,1,1,1,1], 0))
    
    print(bs.get_index([0,1,1,1,1], 0))
    print(bs.get_index([5, 4, 3, 1, 0], 1))
    print(bs.get_index([5, 4, 3, 1, 0], 2))
    
    