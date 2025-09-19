# LC00804_Unique_Morse_Code_Words.py

# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:

# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.",
#  "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". 
# We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.

 

# Example 1:

# Input: words = ["gin","zen","gig","msg"]
# Output: 2
# Explanation: The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# There are 2 different transformations: "--...-." and "--...--.".
# Example 2:

# Input: words = ["a"]
# Output: 1
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 12
# words[i] consists of lowercase English letters.

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        my_set=set()
        Morse_code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.",
                    "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            my_str=''
            for i in range(len(word)):
                my_str=my_str+Morse_code[ord(word[i])-ord('a')]
            if my_str not in my_set:
                my_set.add(my_str)

        return len(my_set)
                

        


