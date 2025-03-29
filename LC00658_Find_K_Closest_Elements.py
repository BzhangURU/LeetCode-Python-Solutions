# LC00658_Find_K_Closest_Elements.py

# Given a sorted integer array arr, two integers k and x, return the k closest 
# integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3

# Output: [1,2,3,4]

# Example 2:

# Input: arr = [1,1,2,3,4,5], k = 4, x = -1

# Output: [1,1,2,3]

 

# Constraints:

# 1 <= k <= arr.length
# 1 <= arr.length <= 10**4
# arr is sorted in ascending order.
# -10**4 <= arr[i], x <= 10**4

# Idea: first get two neighbors that bound the x, then search in both directions.

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x<=arr[0]:
            left_ind=-1
            right_ind=0
        elif x>=arr[-1]:
            left_ind=len(arr)-1
            right_ind=len(arr)
        else:
            left_ind=0
            right_ind=len(arr)
            while left_ind+1<right_ind:
                middle_ind=(left_ind+right_ind)//2
                if arr[middle_ind]<x:
                    left_ind=middle_ind
                elif arr[middle_ind]>x:
                    right_ind=middle_ind
                else:
                    left_ind=middle_ind
                    right_ind=middle_ind+1
        # left_ind and right_ind are not inclusive
        while (left_ind>=0 or right_ind<=len(arr)-1) and right_ind-left_ind-1<k:
            if left_ind<0:
                right_ind+=1
            elif right_ind>len(arr)-1:
                left_ind-=1
            else:
                if x-arr[left_ind]<=arr[right_ind]-x:
                    left_ind-=1
                else:
                    right_ind+=1
        result=arr[left_ind+1:right_ind]
        return result
        


