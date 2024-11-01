
#LC03101_Count_Alternating_Subarrays.py

# You are given a 
# binary array
#  nums.

# We call a 
# subarray
#  alternating if no two adjacent elements in the subarray have the same value.

# Return the number of alternating subarrays in nums.

# A binary array is an array which contains only 0 and 1
# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: nums = [0,1,1,1]

# Output: 5

# Explanation:

# The following subarrays are alternating: [0], [1], [1], [1], and [0,1].

# Example 2:

# Input: nums = [1,0,1,0]

# Output: 10

# Explanation:

# Every subarray of the array is alternating. There are 10 possible subarrays that we can choose.

 

# Constraints:

# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.

# My idea that is not using dynamic programming: separate the binary array into multiple fractions, each fraction is largest alternating subarrays
#for example: 
#0001010101101011101010111111000010100
#0  0   01010101    10101   1   1010101     1   1   1   1   10  0   0   01010   0
#Then sum each fraction's count to get the answer. 
from typing import List

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        frac_num_digits=0
        goal=nums[0]
        result=0

        for i in range(len(nums)):
            if nums[i]==goal:
                frac_num_digits+=1
                goal=1-goal
            else:
                result+=int((1+frac_num_digits)*frac_num_digits/2)
                #print('Add {}'.format((1+frac_num_digits)*frac_num_digits/2))
                frac_num_digits=1

        #print('Check final')
        #process final fraction
        result+=int((1+frac_num_digits)*frac_num_digits/2)
        #print('Add {}'.format((1+frac_num_digits)*frac_num_digits/2))

        return result

nums = [0,1,1,1]
my_solu=Solution()
print(nums)
print(my_solu.countAlternatingSubarrays(nums))
