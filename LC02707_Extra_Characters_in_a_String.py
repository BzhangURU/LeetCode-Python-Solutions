

#LC02707_Extra_Characters_in_a_String

# You are given a 0-indexed string s and a dictionary of words dictionary. 
# You have to break s into one or more non-overlapping substrings such that each substring is 
# present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

# Return the minimum number of extra characters left over if you break up s optimally.

 

# Example 1:

# Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
# Output: 1
# Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. 
# There is only 1 unused character (at index 4), so we return 1.

# Example 2:

# Input: s = "sayhelloworld", dictionary = ["hello","world"]
# Output: 3
# Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. 
# The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
 

# Constraints:

# 1 <= s.length <= 50
# 1 <= dictionary.length <= 50
# 1 <= dictionary[i].length <= 50
# dictionary[i] and s consists of only lowercase English letters
# dictionary contains distinct words

#Idea: use dynamic programming. Define minEC_prefix[i] as minExtraChar of str[0:i], 0<=i<=len(s)

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        
        my_set=set()
        max_word_len=0
        for i in range(len(dictionary)):
            my_set.add(dictionary[i])
            if len(dictionary[i])>max_word_len:
                max_word_len=len(dictionary[i])

        minEC_prefix=[0]*(len(s)+1)
        minEC_prefix[0]=0

        for i in range(1,len(s)+1):
            
            left=max(0,i-max_word_len)

            if s[i-1] in my_set:
                minEC=minEC_prefix[i-1]
            else:
                minEC=minEC_prefix[i-1]+1

            for j in range(left,i-1):
                if s[j:i] in my_set:
                    if minEC_prefix[j]<minEC:
                        minEC=minEC_prefix[j]
            minEC_prefix[i]=minEC

        return minEC_prefix[len(s)]
