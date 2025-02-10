# LC00648_Replace_Words.py

# In English, we have a concept called root, which can be followed by some other word to 
# form another longer word - let's call this word derivative. For example, when the root "help" 
# is followed by the word "ful", we can form a derivative "helpful".

# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, 
# replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced 
# by more than one root, replace it with the root that has the shortest length.

# Return the sentence after the replacement.

 

# Example 1:

# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
# Example 2:

# Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# Output: "a a b c"
 

# Constraints:

# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 100
# dictionary[i] consists of only lower-case letters.
# 1 <= sentence.length <= 10**6
# sentence consists of only lower-case letters and spaces.
# The number of words in sentence is in the range [1, 1000]
# The length of each word in sentence is in the range [1, 1000]
# Every two consecutive words in sentence will be separated by exactly one space.
# sentence does not have leading or trailing spaces.

from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root_set=set()
        min_root_length=len(dictionary[0])
        max_root_length=len(dictionary[0])
        for root in dictionary:
            root_set.add(root)
            if len(root)<min_root_length:
                min_root_length=len(root)
            if len(root)>max_root_length:
                max_root_length=len(root)

        list_words=sentence.split(' ')
        for word_ind, word in enumerate(list_words):
            for i in range(min_root_length,min(max_root_length+1,len(word))):
                if word[0:i] in root_set:
                    list_words[word_ind]=word[0:i]
                    break
        result=' '.join(list_words)
        return result


        
        


