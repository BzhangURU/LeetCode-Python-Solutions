# LC0567_Permutation_in_String.py

# Given two strings s1 and s2, return true if s2 contains a 
# permutation
#  of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.

# Idea: create letter_bins_goal, letter_bins_current. Also define a count_bins_match to check how many bins are matched. 
# for example: bin 'a' has matched count, then count_bins_match+=1

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letter_bins_goal=[0]*26
        letter_bins_current=[0]*26
        for i in range(len(s1)):
            letter_bins_goal[ord(s1[i])-ord('a')]+=1
        
        if len(s2)<len(s1):
            return False

        for i in range(len(s1)):
            letter_bins_current[ord(s2[i])-ord('a')]+=1

        count_bins_match=0
        for i in range(26):
            if letter_bins_current[i]==letter_bins_goal[i]:
                count_bins_match+=1
        if count_bins_match==26:
            return True

        for i in range(len(s1),len(s2)):
            #take new letter at s2[i], pop old letter at s2[i-len(s1)]
            if s2[i]==s2[i-len(s1)]:
                pass
            else:
                new_letter_ASCII=ord(s2[i])
                letter_bins_current[new_letter_ASCII-ord('a')]+=1
                if letter_bins_current[new_letter_ASCII-ord('a')]==letter_bins_goal[new_letter_ASCII-ord('a')]:
                    count_bins_match+=1
                elif letter_bins_current[new_letter_ASCII-ord('a')]-1==letter_bins_goal[new_letter_ASCII-ord('a')]:
                    count_bins_match-=1

                old_letter_ASCII=ord(s2[i-len(s1)])
                letter_bins_current[old_letter_ASCII-ord('a')]-=1
                if letter_bins_current[old_letter_ASCII-ord('a')]==letter_bins_goal[old_letter_ASCII-ord('a')]:
                    count_bins_match+=1
                elif letter_bins_current[old_letter_ASCII-ord('a')]+1==letter_bins_goal[old_letter_ASCII-ord('a')]:
                    count_bins_match-=1

                if count_bins_match==26:
                    return True
        return False



