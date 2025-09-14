# LC00792_Number_of_Matching_Subsequences.py

# Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) 
# deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
 

# Example 1:

# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
# Example 2:

# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2
 

# Constraints:

# 1 <= s.length <= 5 * 10**4
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# s and words[i] consist of only lowercase English letters.

# Idea: for each lowercase English letter, save its occurred indexes in a list, then during searching words[i],
# while searching a letter, just use binary search to get the earliest position in s.  

class Solution:
    def find_smallest_num_in_sorted_list_larger_than_thresh(self, sorted_list,thresh):
        #binary search
        if len(sorted_list)==0:
            return -1
        left_ind=0
        right_ind=len(sorted_list)-1
        if sorted_list[left_ind]>thresh:
            return sorted_list[left_ind]
        if sorted_list[right_ind]<=thresh:
            return -1
        while left_ind<right_ind-1:
            middle_ind=(left_ind+right_ind)//2
            if sorted_list[middle_ind]>thresh:
                right_ind=middle_ind
            else:
                left_ind=middle_ind
        return sorted_list[right_ind]

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        s_each_letter_positions=[[] for i in range(26)]
        for i in range(len(s)):
            s_each_letter_positions[ord(s[i])-ord('a')].append(i)
        output=0
        for word in words:
            last_pos=-1
            isSubSeq=True
            for i in range(len(word)):
                new_pos=self.find_smallest_num_in_sorted_list_larger_than_thresh(s_each_letter_positions[ord(word[i])-ord('a')],last_pos)
                if new_pos==-1:
                    isSubSeq=False
                    break
                last_pos=new_pos
            if isSubSeq:
                output+=1
        return output
            
