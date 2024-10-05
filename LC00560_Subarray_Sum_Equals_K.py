
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7

def subarraySum(nums, k):
    sum_prev=0
    count=0
    sum_freq={0:1}
    
    for i in range(len(nums)):
        sum_prev+=nums[i]
        if sum_prev-k in sum_freq:
            #we add number of qualified subarrays whose last element is current index i 
            count+=sum_freq[sum_prev-k]
            
        #update sum_freq
        if sum_prev in sum_freq:
            sum_freq[sum_prev]+=1
        else:
            sum_freq[sum_prev]=1
    return count
if __name__=="__main__":
    nums=[1,2,3]
    k=3
    print(subarraySum(nums, k))
