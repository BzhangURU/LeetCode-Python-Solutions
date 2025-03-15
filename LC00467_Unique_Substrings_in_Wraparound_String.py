# LC00467_Unique_Substrings_in_Wraparound_String.py

# We define the string base to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", 
# so base will look like this:

# "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
# Given a string s, return the number of unique non-empty substrings of s are present in base.

 

# Example 1:

# Input: s = "a"
# Output: 1
# Explanation: Only the substring "a" of s is in base.
# Example 2:

# Input: s = "cac"
# Output: 2
# Explanation: There are two substrings ("a", "c") of s in base.
# Example 3:

# Input: s = "zab"
# Output: 6
# Explanation: There are six substrings ("z", "a", "b", "za", "ab", and "zab") of s in base.
 

# Constraints:

# 1 <= s.length <= 10**5
# s consists of lowercase English letters.

# Idea: First divide string into multiple parts, each part follows "...xyzabcd..." order
# then, for each char, check the length start from here to the end of current part, update the 
# dictionary:
# start from a, we have all substrings with length 1-23
# start from b, we have all substrings with length 1-4
# start from c, we have all substrings with length 1-7

# then we finally calculate the sum of 23+4+7+...

class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        each_part_start_ind=[0]
        for i in range(1,len(s)):
            if ord(s[i])!=ord(s[i-1])+1 and ord(s[i])!=ord(s[i-1])-26+1:
                each_part_start_ind.append(i)
        each_part_start_ind.append(len(s))

        count_26_lengths=[0]*26

        for part_ind in range(len(each_part_start_ind)-1):
            start_ind=each_part_start_ind[part_ind]
            end_ind=each_part_start_ind[part_ind+1]

            for i in range(start_ind,end_ind):
                if end_ind-i>count_26_lengths[ord(s[i])-ord('a')]:
                    count_26_lengths[ord(s[i])-ord('a')]=end_ind-i

        result=sum(count_26_lengths)
        return result


        




