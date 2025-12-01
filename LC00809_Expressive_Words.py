# LC00809_Expressive_Words.py

# Sometimes people repeat letters to represent extra feeling. For example:

# "hello" -> "heeellooo"
# "hi" -> "hiiii"
# In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

# You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s 
# by any number of applications of the following extension operation: choose a group consisting of characters c, and add 
# some number of characters c to the group so that the size of the group is three or more.

# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" 
# since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". 
# If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: 
# query = "hello" -> "hellooo" -> "helllllooo" = s.
# Return the number of query strings that are stretchy.

 

# Example 1:

# Input: s = "heeellooo", words = ["hello", "hi", "helo"]
# Output: 1
# Explanation: 
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
# Example 2:

# Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
# Output: 3
 

# Constraints:

# 1 <= s.length, words.length <= 100
# 1 <= words[i].length <= 100
# s and words[i] consist of lowercase letters.

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        #First, change s to char and frequency
        char_freq=[]
        freq=0
        for i in range(len(s)):
            freq+=1
            if i==len(s)-1 or s[i]!=s[i+1]:
                char_freq.append((s[i],freq))
                freq=0

        output=0
        for word in words:
            freq=0
            s__char_ind=0
            stretchy=True
            for i in range(len(word)):
                freq+=1
                if i==len(word)-1 or word[i]!=word[i+1]:
                    if s__char_ind>=len(char_freq):
                        stretchy=False
                        break
                    if char_freq[s__char_ind][0]!=word[i]:
                        stretchy=False
                        break
                    if char_freq[s__char_ind][1]<3 and char_freq[s__char_ind][1]!=freq:
                        stretchy=False
                        break
                    if char_freq[s__char_ind][1]<freq:
                        stretchy=False
                        break
                    s__char_ind+=1
                    freq=0
            if stretchy and s__char_ind==len(char_freq):
                output+=1
        return output


