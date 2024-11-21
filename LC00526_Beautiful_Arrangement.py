# LC00526_Beautiful_Arrangement.py

# Suppose you have n integers labeled 1 through n. A permutation of 
# those n integers perm (1-indexed) is considered a beautiful arrangement 
# if for every i (1 <= i <= n), either of the following is true:

# perm[i] is divisible by i.
# i is divisible by perm[i].
# Given an integer n, return the number of the beautiful arrangements that you can construct.

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: 
# The first beautiful arrangement is [1,2]:
#     - perm[1] = 1 is divisible by i = 1
#     - perm[2] = 2 is divisible by i = 2
# The second beautiful arrangement is [2,1]:
#     - perm[1] = 2 is divisible by i = 1
#     - i = 2 is divisible by perm[2] = 1
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 15

def count_perm(my_dict, set_used_nums, n, index):

    #index==n
    if index==n:
        #find the last num that is not used
        last_num=0
        for num in range(1,n+1):
            if num not in set_used_nums:
                last_num=num

        if last_num in my_dict[index]:
            return 1
        else:
            return 0
    #  
    count=0
    #index start from 1
    for num in my_dict[index]:
        if num not in set_used_nums:
            set_used_nums.add(num)
            count+=count_perm(my_dict, set_used_nums,n,index+1)
            set_used_nums.remove(num)

    return count


class Solution:
    def countArrangement(self, n: int) -> int:
        

        #First, count each slot's possible number, save them to dict. 

        my_dict={}
        for i in range(1,n+1):
            my_dict[i]=set()
            for j in range(1,n+1):
                if i%j==0 or j%i==0:
                    my_dict[i].add(j)

        #Second, check all possibilities by index from start to end
        set_used_nums=set()
        return count_perm(my_dict, set_used_nums, n, 1)
