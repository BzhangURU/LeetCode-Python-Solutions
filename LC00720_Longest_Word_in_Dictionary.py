# LC00720_Longest_Word_in_Dictionary.py

# Given an array of strings words representing an English Dictionary, 
# return the longest word in words that can be built one character at a time by other words in words.

# If there is more than one possible answer, return the longest word 
# with the smallest lexicographical order. If there is no answer, return the empty string.

# Note that the word should be built from left to right with each 
# additional character being added to the end of a previous word. 

 

# Example 1:

# Input: words = ["w","wo","wor","worl","world"]
# Output: "world"
# Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
# Example 2:

# Input: words = ["a","banana","app","appl","ap","apply","apple"]
# Output: "apple"
# Explanation: Both "apply" and "apple" can be built from other words in 
# the dictionary. However, "apple" is lexicographically smaller than "apply".
 

# Constraints:

# 1 <= words.length <= 1000
# 1 <= words[i].length <= 30
# words[i] consists of lowercase English letters.

class Solution:
    def longestWord(self, words: List[str]) -> str:
        my_set=set(words)
        result=''
        for i in range(len(words)):
            cur_word=words[i]
            can_be_built=True
            for ind in range(len(cur_word)):
                if cur_word[:ind+1] not in my_set:
                    can_be_built=False
                    break
            if can_be_built:
                if len(cur_word)>len(result):
                    result=cur_word
                elif len(cur_word)==len(result) and cur_word<result:
                    result=cur_word
        return result


        

