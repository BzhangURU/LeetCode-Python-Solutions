# LC00524_Longest_Word_in_Dictionary_through_Deleting.py

# Given a string s and a string array dictionary, return the longest string in the 
# dictionary that can be formed by deleting some of the given string characters. 
# If there is more than one possible result, return the longest word with the smallest 
# lexicographical order. If there is no possible result, return the empty string.


# Example 1:

# Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
# Output: "apple"
# Example 2:

# Input: s = "abpcplea", dictionary = ["a","b","c"]
# Output: "a"
 

# Constraints:

# 1 <= s.length <= 1000
# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 1000
# s and dictionary[i] consist of lowercase English letters.

from functools import cmp_to_key

def cmp_str(str1,str2):
    if len(str1)!=len(str2):
        return len(str2)-len(str1)
    else:
        for i in range(len(str1)):
            if str1[i]!=str2[i]:
                return ord(str1[i])-ord(str2[i])
        return 0

def str_in_s(dict_str, s):
    str_ind=0
    for i in range(len(s)):
        if s[i]==dict_str[str_ind]:
            str_ind+=1
            if str_ind==len(dict_str):
                return True
    return False

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        sorted_dict=sorted(dictionary, key=cmp_to_key(cmp_str))
        for dict_str in sorted_dict:
            if str_in_s(dict_str,s):
                return dict_str
        return ""
