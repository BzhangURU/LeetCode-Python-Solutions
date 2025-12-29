# LC00819_Most_Common_Word.py

# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. 
# It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

# Note that words can not contain punctuation symbols.

 

# Example 1:

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.
# Example 2:

# Input: paragraph = "a.", banned = []
# Output: "a"
 

# Constraints:

# 1 <= paragraph.length <= 1000
# paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
# 0 <= banned.length <= 100
# 1 <= banned[i].length <= 10
# banned[i] consists of only lowercase English letters.


class Solution:
    def isLowerLetter(self, my_char):
        if ord(my_char)>=ord('a') and ord(my_char)<=ord('z'):
            return True
        else:
            return False
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        dict_word_freq={}
        start_word_ind=0
        set_banned=set(banned)
        for i in range(len(paragraph)):
            if (i==0 and self.isLowerLetter(paragraph[i])) or (self.isLowerLetter(paragraph[i]) and not self.isLowerLetter(paragraph[i-1])):
                start_word_ind=i
            if (i==len(paragraph)-1 and self.isLowerLetter(paragraph[i])) or (self.isLowerLetter(paragraph[i]) and not self.isLowerLetter(paragraph[i+1])):
                new_word=paragraph[start_word_ind:i+1]
                if new_word not in set_banned:
                    if new_word in dict_word_freq:
                        dict_word_freq[new_word]+=1
                    else:
                        dict_word_freq[new_word]=1
        max_word=''
        max_freq=0
        for k, v in dict_word_freq.items():
            if v>max_freq:
                max_freq=v
                max_word=k
        return max_word

                
            


