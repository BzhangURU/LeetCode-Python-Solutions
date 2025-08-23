# LC00748_Shortest_Completing_Word.py

# Given a string licensePlate and an array of strings words, find the shortest completing word in words.

# A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces 
# in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, 
# then it must appear in the word the same number of times or more.

# For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. 
# Possible completing words are "abccdef", "caaacab", and "cbca".

# Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple 
# shortest completing words, return the first one that occurs in words.

 

# Example 1:

# Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
# Output: "steps"
# Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
# "step" contains 't' and 'p', but only contains 1 's'.
# "steps" contains 't', 'p', and both 's' characters.
# "stripe" is missing an 's'.
# "stepple" is missing an 's'.
# Since "steps" is the only word containing all the letters, that is the answer.
# Example 2:

# Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
# Output: "pest"
# Explanation: licensePlate only contains the letter 's'. All the words contain 's', 
# but among these "pest", "stew", and "show" are shortest. The answer is "pest" 
# because it is the word that appears earliest of the 3.
 

# Constraints:

# 1 <= licensePlate.length <= 7
# licensePlate contains digits, letters (uppercase or lowercase), or space ' '.
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 15
# words[i] consists of lower case English letters.


# from functools import cmp_to_key

# def my_cmp(x,y):
#     return len(x)-len(y)

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate=licensePlate.lower()
        letter_dict={}
        for i in range(len(licensePlate)):
            if ord('a')<=ord(licensePlate[i]) and ord(licensePlate[i])<=ord('z'):
                if licensePlate[i] not in letter_dict:
                    letter_dict[licensePlate[i]]=1
                else:
                    letter_dict[licensePlate[i]]+=1

        words.sort(lambda p: len(p))
        # words.sort(key=cmp_to_key(my_cmp))
        
        for word in words:
            qualified=True
            for k,v in letter_dict.items():
                count=0
                for i in range(len(word)):
                    if word[i]==k:
                        count+=1
                if count<v:
                    qualified=False
                    break
            if qualified:
                return word
        return -1
            

