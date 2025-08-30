# LC00768_Max_Chunks_To_Make_Sorted_II.py

# You are given an integer array arr.

# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. 
# After concatenating them, the result should equal the sorted array.

# Return the largest number of chunks we can make to sort the array.

 

# Example 1:

# Input: arr = [5,4,3,2,1]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
# Example 2:

# Input: arr = [2,1,3,4,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [2, 1], [3, 4, 4].
# However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
 

# Constraints:

# 1 <= arr.length <= 2000
# 0 <= arr[i] <= 10**8

# Idea: similar idea as LC00769, just be careful of duplicated number

# for example:   0 2 3 4 4 4 1 8 9, when you reach 2 3 4 4, the i==max==4, but not a good candidate
# we get a helper array that get min of "4 1 8 9", if min >=4, then it is a good chunk. otherwise not. 

# another idea: we also should have sorted array 0 1 2 3 4 4 4 8 9, 
# when we reach 2 3 4 4 in unsorted array, we need to make sure [2,3,4,4].count(4)==[1 2 3 4].count(4) or not.

from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr=sorted(arr)
        output=0
        min_start_from=[arr[-1] for i in range(len(arr))]
        min_num=arr[-1]
        for i in range(len(arr)-2, -1, -1):
            if arr[i]<min_num:
                min_num=arr[i]
            min_start_from[i]=min_num
        max_num=-1
        for i in range(len(arr)):
            if arr[i]>max_num:
                max_num=arr[i]
            if max_num==sorted_arr[i] and (i==len(arr)-1 or min_start_from[i+1]>=sorted_arr[i]):
                output+=1
                max_num=-1
        return output
