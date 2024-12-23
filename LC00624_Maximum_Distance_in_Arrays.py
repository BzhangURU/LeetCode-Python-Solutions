# LC00624_Maximum_Distance_in_Arrays.py

# You are given m arrays, where each array is sorted in ascending order.

# You can pick up two integers from two different arrays (each array picks one) 
# and calculate the distance. We define the distance between two integers a 
# and b to be their absolute difference |a - b|.

# Return the maximum distance.

 

# Example 1:

# Input: arrays = [[1,2,3],[4,5],[1,2,3]]
# Output: 4
# Explanation: One way to reach the maximum distance 4 is 
# to pick 1 in the first or third array and pick 5 in the second array.
# Example 2:

# Input: arrays = [[1],[1]]
# Output: 0
 

# Constraints:

# m == arrays.length
# 2 <= m <= 10**5
# 1 <= arrays[i].length <= 500
# -10**4 <= arrays[i][j] <= 10**4
# arrays[i] is sorted in ascending order.
# There will be at most 10**5 integers in all the arrays.

#Idea: find global max and global min, if they come from dif array, then that's the answer.
#otherwise, first try using global max, then check global min not in current array, 
#then try using global min, then check global max not in current array, 

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max0=max(arrays[0])
        max1=max(arrays[1])
        if max0>max1:
            global_max=max0
            global_max_array_index=0
            global_secondary_max=max1
            #global_secondary_min_array_index=1
        else:
            global_max=max1
            global_max_array_index=1
            global_secondary_max=max0
            #global_secondary_min_array_index=0

        min0=min(arrays[0])
        min1=min(arrays[1])
        if min0<min1:
            global_min=min0
            global_min_array_index=0
            global_secondary_min=min1
            #global_secondary_min_array_index=1
        else:
            global_min=min1
            global_min_array_index=1
            global_secondary_min=min0
            #global_secondary_min_array_index=0

        for array_ind in range(2, len(arrays)):
            one_array_max=max(arrays[array_ind])
            if one_array_max>global_max:
                global_secondary_max=global_max
                #global_secondary_max_array_index=global_max_array_index
                global_max=one_array_max
                global_max_array_index=array_ind
            elif one_array_max>global_secondary_max:
                global_secondary_max=one_array_max
                #global_secondary_max_array_index=array_ind
            one_array_min=min(arrays[array_ind])
            if one_array_min<global_min:
                global_secondary_min=global_min
                #global_secondary_min_array_index=global_min_array_index
                global_min=one_array_min
                global_min_array_index=array_ind
            elif one_array_min<global_secondary_min:
                global_secondary_min=one_array_min
                #global_secondary_min_array_index=array_ind
        # print(global_max,global_secondary_max)
        # print(global_secondary_max,global_secondary_min)
        # print(global_max_array_index,global_min_array_index)
                
        if global_min_array_index!=global_max_array_index:
            return global_max-global_min
        else:
            return max(global_max-global_secondary_min,
                       global_secondary_max-global_min)


            

        
