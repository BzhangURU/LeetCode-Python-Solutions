# LC00710_Random_Pick_with_Blacklist.py

# You are given an integer n and an array of unique integers blacklist. 
# Design an algorithm to pick a random integer in the range [0, n - 1] 
# that is not in blacklist. Any integer that is in the mentioned range 
# and not in blacklist should be equally likely to be returned.

# Optimize your algorithm such that it minimizes the number of calls to the built-in 
# random function of your language.

# Implement the Solution class:

# Solution(int n, int[] blacklist) Initializes the object with the integer n and 
# the blacklisted integers blacklist.
# int pick() Returns a random integer in the range [0, n - 1] and not in blacklist.
 

# Example 1:

# Input
# ["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
# [[7, [2, 3, 5]], [], [], [], [], [], [], []]
# Output
# [null, 0, 4, 1, 6, 1, 0, 4]

# Explanation
# Solution solution = new Solution(7, [2, 3, 5]);
# solution.pick(); // return 0, any integer from [0,1,4,6] should be ok. Note that for every call of pick,
#                  // 0, 1, 4, and 6 must be equally likely to be returned (i.e., with probability 1/4).
# solution.pick(); // return 4
# solution.pick(); // return 1
# solution.pick(); // return 6
# solution.pick(); // return 1
# solution.pick(); // return 0
# solution.pick(); // return 4
 

# Constraints:

# 1 <= n <= 10**9
# 0 <= blacklist.length <= min(10**5, n - 1)
# 0 <= blacklist[i] < n
# All the values of blacklist are unique.
# At most 2 * 10**4 calls will be made to pick.


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()

from typing import List


# Idea: 
# 1. random select a number, if in blacklist, select again, but if available portion is small, takes more time.
# 2. save a one-one mapping that skips all numbers in blacklist, but if n is very large, take more time. 
# 3. the blacklist separated multiple chunks in [1,n], we first randomly select a chunk with weights, then randomly
#    select a number in the chunk.  
import random
class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        blacklist.sort()
        total_available_numbers=float(n-len(blacklist))
        #accumulated_fraction=0.0
        accumulated_numbers=0
        self.chunks=[]
        start_num=0
        for i in range(len(blacklist)):
            if blacklist[i]!=start_num:
                frac_start=float(accumulated_numbers)/total_available_numbers #accumulated_fraction
                frac_end=frac_start+float(blacklist[i]-start_num)/total_available_numbers
                self.chunks.append([frac_start,frac_end,start_num,blacklist[i]])

                accumulated_numbers+=blacklist[i]-start_num
                start_num=blacklist[i]+1
                #accumulated_fraction=frac_end
                
            else:
                start_num=blacklist[i]+1

        if len(blacklist)==0 or blacklist[-1]<n-1:
            frac_start=float(accumulated_numbers)/total_available_numbers#accumulated_fraction
            frac_end=1.0#frac_start+float(n-start_num)/total_available_numbers
            self.chunks.append([frac_start,frac_end,start_num,n])
        #if n==20000 and len(blacklist)>0 and blacklist[0]==7609:
        print(len(blacklist))
        print(self.chunks)

    def get_chunk(self,chunks,random01):
        left_ind=0
        right_ind=len(chunks)-1
        if chunks[left_ind][0]<=random01 and random01<chunks[left_ind][1]:
            return left_ind
        if chunks[right_ind][0]<=random01 and random01<=chunks[right_ind][1]:
            return right_ind
        while left_ind!=right_ind:
            middle_ind=(left_ind+right_ind)//2
            if chunks[middle_ind][0]<=random01 and random01<chunks[middle_ind][1]:
                return middle_ind
            elif random01<chunks[middle_ind][0]:
                right_ind=middle_ind
            elif chunks[middle_ind][1]<=random01:
                left_ind=middle_ind
        return -1#wrong

    def pick(self) -> int:
        random01=random.uniform(0.0,1.0)
        print(random01)
        chunk_ind=self.get_chunk(self.chunks,random01)
        print(chunk_ind)
        cur_chunk_size=self.chunks[chunk_ind][3]-self.chunks[chunk_ind][2]
        random_num=random.randrange(cur_chunk_size)
        return self.chunks[chunk_ind][2]+random_num
