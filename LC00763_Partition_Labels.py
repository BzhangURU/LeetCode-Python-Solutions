# LC00763_Partition_Labels.py

# You are given a string s. We want to partition the string into as many parts as possible so that 
# each letter appears in at most one part. For example, the string "ababcc" can be partitioned into 
# ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

# Note that the partition is done so that after concatenating all the parts in order, the resultant 
# string should be s.

# Return a list of integers representing the size of these parts.

 

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
# Example 2:

# Input: s = "eccbbbbdec"
# Output: [10]
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.

#Idea: start from first letter, check its last existing index, then scan until it. If during scanning, you
#find other letters, also check their last existing indexes, update the global last existing index by getting max. 

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dict_letter_first_last={}
        for i in range(len(s)):
            if s[i] not in dict_letter_first_last:
                dict_letter_first_last[s[i]]=[i,i]
            else:
                dict_letter_first_last[s[i]][1]=i

        output=[]
        count=0
        for i in range(len(s)):
            if count==0:
                last_index=dict_letter_first_last[s[i]][1]
                count+=1
                if last_index==i:
                    output.append(count)
                    count=0
            else:
                count+=1
                if last_index>=dict_letter_first_last[s[i]][1]:
                    if i==last_index:
                        output.append(count)
                        count=0
                else:
                    last_index=dict_letter_first_last[s[i]][1]
        # if count!=0:
        #     output.append(count)
        return output

#s = "ababcbacadefegdehijhklij"
s = "caedbdedda"
my_solu=Solution()
print(my_solu.partitionLabels(s))
                
# ababcbaca defegdehijhklij
        
