# LC00474_Ones_and_Zeroes.py

# You are given an array of binary strings strs and two integers m and n.

# Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

# A set x is a subset of a set y if all elements of x are also elements of y.

 

# Example 1:

# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
# Example 2:

# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 

# Constraints:

# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] consists only of digits '0' and '1'.
# 1 <= m, n <= 100

# Idea: f(m,n) is the answer. During iteration, we use a set to save all current f.
# For example, if currently we have f(0,0)=0, f(5,3)=1, f(3,5)=1, f(8,8)=2, then current element is 2,4
# then the updated set will be f(0,0)=0, f(5,3)=1, f(3,5)=1, f(8,8)=2, f(2,4)=1, f(7,7)=2, f(5,9)=2, f(10,12)=3
# The "f(8,8)=2" is not deleted even though we have "f(7,7)=2" because it takes a lot of time to scan and delete
# But we will update the value if for example we have "f(8,8)=3"
# Finally, we iterate the set and find the largest value in f. (even if it is not f(m,n), but like f(m-2,n-1))

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        my_dict={(0,0):0}

        for i in range(len(strs)):
            count_zeros=strs[i].count('0')
            count_ones=strs[i].count('1')
            if count_zeros>m or count_ones>n:
                pass
            new_dict=my_dict.copy()
            for k,v in my_dict.items():
                if k[0]+count_zeros<=m and k[1]+count_ones<=n:
                    if (k[0]+count_zeros, k[1]+count_ones) not in new_dict:
                        new_dict[(k[0]+count_zeros, k[1]+count_ones)]=v+1
                    elif v+1>new_dict[(k[0]+count_zeros, k[1]+count_ones)]:
                        new_dict[(k[0]+count_zeros, k[1]+count_ones)]=v+1
            my_dict=new_dict

        result=0
        for k,v in my_dict.items():
            if v>result:
                result=v

        return result
            


        
