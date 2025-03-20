# LC00639_Decode_Ways_II.py

# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into 
# letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# In addition to the mapping above, an encoded message may contain the '*' character, which can 
# represent any digit from '1' to '9' ('0' is excluded). For example, the encoded message "1*" may 
# represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19". 
# Decoding "1*" is equivalent to decoding any of the encoded messages it can represent.

# Given a string s consisting of digits and '*' characters, return the number of ways to decode it.

# Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: s = "*"
# Output: 9
# Explanation: The encoded message can represent any of the encoded messages "1", "2", "3", "4", "5", "6", "7", "8", or "9".
# Each of these can be decoded to the strings "A", "B", "C", "D", "E", "F", "G", "H", and "I" respectively.
# Hence, there are a total of 9 ways to decode "*".
# Example 2:

# Input: s = "1*"
# Output: 18
# Explanation: The encoded message can represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", 
# or "19".
# Each of these encoded messages have 2 ways to be decoded (e.g. "11" can be decoded to "AA" or "K").
# Hence, there are a total of 9 * 2 = 18 ways to decode "1*".
# Example 3:

# Input: s = "2*"
# Output: 15
# Explanation: The encoded message can represent any of the encoded messages "21", "22", "23", "24", "25", "26", "27", "28", 
# or "29".
# "21", "22", "23", "24", "25", and "26" have 2 ways of being decoded, but "27", "28", and "29" only have 1 way.
# Hence, there are a total of (6 * 2) + (3 * 1) = 12 + 3 = 15 ways to decode "2*".
 

# Constraints:

# 1 <= s.length <= 10**5
# s[i] is a digit or '*'.

# Idea: DP. 
# f(xxxabcde)=f(xxxabcd)*f(e)+f(xxxabc)*(de)

def two_chars_to_letters(char1,char2):
    if char1=='0':
        return 0
    elif char1=='1':
        if char2=='*':
            return 9
        else:
            return 1
    elif char1=='2':
        if char2=='*':
            return 6
        elif ord(char2)<=ord('6'):
            return 1
        else:
            return 0
    elif char1=='*':
        if char2=='*':
            return 15 #'*' can't be zero, 9+6
        elif ord(char2)<=ord('6'):
            return 2 #1+1
        else:
            return 1 #1+0
    else:
        return 0
    
def one_char_to_letters(char1):
    if char1=='*':
        return 9
    elif char1=='0':
        return 0
    else:
        return 1


class Solution:
    def numDecodings(self, s: str) -> int:
        #return self.my_num_decodings(s,0,len(s))
        if len(s)==0:
            #zero char
            return 1
        elif len(s)==1:
            #one char
            if s=='*':
                return 9
            elif s=='0':
                return 0
            else:
                return 1
        else:
            dp=[0]*len(s)
            dp[0]=self.numDecodings(s[0])

            for i in range(1,len(s)):
                dp[i]+=dp[i-1]*one_char_to_letters(s[i])
                two_chars_types=two_chars_to_letters(s[i-1],s[i])
                if two_chars_types>0:
                    if i==1:
                        dp[1]+=two_chars_types
                    else:
                        dp[i]+=dp[i-2]*two_chars_types
                dp[i]%=(10**9+7)
            return dp[len(s)-1]

