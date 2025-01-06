# LC00500_Keyboard_Row.py
# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

 

# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]

# Output: ["Alaska","Dad"]

# Explanation:

# Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.

# Example 2:

# Input: words = ["omk"]

# Output: []

# Example 3:

# Input: words = ["adsdf","sfd"]

# Output: ["adsdf","sfd"]

 

# Constraints:

# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] consists of English letters (both lowercase and uppercase). 

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set_first_row=set(['q','w','e','r','t','y','u','i','o','p'])
        set_second_row=set(list("asdfghjkl"))
        set_third_row=set(list("zxcvbnm"))
        result=[]
        for wordUL in words:
            word=wordUL.lower()
            same_row=True
            if word[0] in set_first_row:
                set_target=set_first_row
            elif word[0] in set_second_row:
                set_target=set_second_row
            elif word[0] in set_third_row:
                set_target=set_third_row
            else:
                print(f'Wrong word {wordUL}')
            for i in range(1,len(word)):
                if word[i] not in set_target:
                    same_row=False
                    break
            if same_row:
                result.append(wordUL)
        return result

