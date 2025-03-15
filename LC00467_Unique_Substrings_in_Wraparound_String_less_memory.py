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

    # less memory version:
    def findSubstringInWraproundString(self, s: str) -> int:
        count_26_lengths=[0]*26
        end_ind_in_cur_part=0
        for i in range(len(s)):
            if i == end_ind_in_cur_part:
                # go find new part's end_ind_in_cur_part
                for j in range(end_ind_in_cur_part+1, len(s)+1):
                    if j==len(s):
                        end_ind_in_cur_part=len(s)
                        break
                    if ord(s[j])!=ord(s[j-1])+1 and ord(s[j])!=ord(s[j-1])-26+1:
                        end_ind_in_cur_part=j
                        break
                    
            if end_ind_in_cur_part-i>count_26_lengths[ord(s[i])-ord('a')]:
                count_26_lengths[ord(s[i])-ord('a')]=end_ind_in_cur_part-i

        result=sum(count_26_lengths)
        return result


        




