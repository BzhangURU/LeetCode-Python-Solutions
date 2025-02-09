# LC00451_Sort_Characters_By_Frequency.py

# Given a string s, sort it in decreasing order based on the frequency of the characters. 
# The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

 

# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
 

# Constraints:

# 1 <= s.length <= 5 * 10**5
# s consists of uppercase and lowercase English letters and digits.

from heapq import *

class Solution:
    def frequencySort(self, s: str) -> str:
        dict_char_freq={}
        for i in range(len(s)):
            if s[i] not in dict_char_freq:
                dict_char_freq[s[i]]=1
            else:
                dict_char_freq[s[i]]+=1

        my_heap=[]

        for c,f in dict_char_freq.items():
            my_string=''.join([c]*f)
            heappush(my_heap,(-f, my_string))
        #print(my_heap)
        # [(-2, 'ee'), (-1, 't'), (-1, 'r')]
        my_list_sorted=nsmallest(len(my_heap),my_heap)
        my_list=[tup[1] for tup in my_list_sorted]
        result=''.join(my_list)

        return result

my_solu=Solution()
print(my_solu.frequencySort("raaeaedere"))
        

