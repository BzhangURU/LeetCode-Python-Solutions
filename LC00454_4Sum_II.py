# LC00454_4Sum_II.py

# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, 
# return the number of tuples (i, j, k, l) such that:

# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

# Example 1:

# Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# Output: 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
# Example 2:

# Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# Output: 1
 

# Constraints:

# n == nums1.length
# n == nums2.length
# n == nums3.length
# n == nums4.length
# 1 <= n <= 200
# -2**28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2**28

# Idea: Time Limit exceed: sort, then two-sum
# Be careful, maybe there are duplicated numbers. 

# New idea: first, calculate all possible sums between nums1 and nums2, and each sums' number of tuples. (save to dictionary)
# do the same for nums3 and nums4. Then, iterate the dictionary, compare with the other dictionary to get results.
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dict_12={}
        dict_34={}
        for i1 in range(len(nums1)):
            for i2 in range(len(nums2)):
                two_sum=nums1[i1]+nums2[i2]
                if two_sum not in dict_12:
                    dict_12[two_sum]=1
                else:
                    dict_12[two_sum]+=1

        for i3 in range(len(nums3)):
            for i4 in range(len(nums4)):
                two_sum=nums3[i3]+nums4[i4]
                if two_sum not in dict_34:
                    dict_34[two_sum]=1
                else:
                    dict_34[two_sum]+=1
        result=0
        for two_sum, freq in dict_12.items():
            if -two_sum in dict_34:
                result+=freq*dict_34[-two_sum]
        return result
    # def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    #     nums1.sort()
    #     nums2.sort()
    #     nums3.sort()
    #     nums4.sort()
    #     result=0
    #     for i3 in range(len(nums3)):
    #         for i4 in range(len(nums4)):

    #             #i1=0
    #             i2=len(nums2)-1
    #             for i1 in range(len(nums1)):
    #                 while nums1[i1]+nums2[i2]+nums3[i3]+nums4[i4]>0:
    #                     i2-=1
    #                     if i2<0:
    #                         break
    #                 if i2>=0:
                        
    #                     if nums1[i1]+nums2[i2]+nums3[i3]+nums4[i4]==0:
    #                         result+=1
    #                         # maybe there are duplicated numbers. 
    #                         temp_i2=i2-1
    #                         while temp_i2>=0:
    #                             if nums1[i1]+nums2[temp_i2]+nums3[i3]+nums4[i4]==0:
    #                                 result+=1
    #                             temp_i2-=1
    #     return result 


        

