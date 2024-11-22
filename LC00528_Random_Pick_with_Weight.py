# LC00528_Random_Pick_with_Weight.py

# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

# You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

# For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), 
# and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
 

# Example 1:

# Input
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output
# [null,0]

# Explanation
# Solution solution = new Solution([1]);
# solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
# Example 2:

# Input
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output
# [null,1,1,1,1,0]

# Explanation
# Solution solution = new Solution([1, 3]);
# solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

# Since this is a randomization problem, multiple answers are allowed.
# All of the following outputs can be considered correct:
# [null,1,1,1,1,0]
# [null,1,1,1,1,1]
# [null,1,1,1,0,0]
# [null,1,1,1,0,1]
# [null,1,0,1,0,0]
# ......
# and so on.
 

# Constraints:

# 1 <= w.length <= 10^4
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 104 times.

#Idea: first randomly pick a num in sum(W), then use bisection method to search its index
import random
class Solution:
    def __init__(self, w: List[int]):

        collected_sum=0

        # sum before w[index]
        self.dict_index_to_collected_sum={}

        for i in range(len(w)):
            self.dict_index_to_collected_sum[i]=collected_sum
            collected_sum+=w[i]

        self.total_sum=collected_sum
        self.w=w
        

    def pickIndex(self) -> int:
        rand_num=random.randrange(self.total_sum)

        left=0
        right=len(self.w)-1

        #if rand_num is captured by index left
        if self.dict_index_to_collected_sum[left]<=rand_num and self.dict_index_to_collected_sum[left]+self.w[left]>rand_num:
            return left

        if self.dict_index_to_collected_sum[right]<=rand_num and self.dict_index_to_collected_sum[right]+self.w[right]>rand_num:
            return right

        while left!=right:
            middle=int((left+right)/2)

            if self.dict_index_to_collected_sum[middle]<=rand_num and self.dict_index_to_collected_sum[middle]+self.w[middle]>rand_num:
                return middle
            elif self.dict_index_to_collected_sum[middle]>rand_num:
                right=middle
            else:
                left=middle

        #error
        return -1

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
