# LC00394_Decode_String.py

# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets 
# is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square 
# brackets are well-formed, etc. Furthermore, you may assume that the original data does not 
# contain any digits and that digits are only for those repeat numbers, k. For example, 
# there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
 

# Constraints:

# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].

def char_type(char):
    #0:num
    #1:letter
    #2:left bracket
    #3:right bracket
    if ord(char)>=ord('0') and ord(char)<=ord('9'):
        return 0
    elif ord(char)>=ord('a') and ord(char)<=ord('z'):
        return 1
    elif char=='[':
        return 2
    else:
        return 3

class Solution:
    def decodeString(self, s: str) -> str:
        if s.find('[')<0:
            return s
        # first, change '3[ab2[c]]de4[f]' to '3.[ab2[c]].de.44.[f]'
        count_left_bracket=0
        count_right_bracket=0
        list_char=list(s)

        prev_type=char_type(list_char[0])
        list_char2=[list_char[0]]
        for i in range(1,len(list_char)):
            cur_type=char_type(list_char[i])
            if count_left_bracket==count_right_bracket and prev_type!=cur_type:
                list_char2.append('.')
            list_char2.append(list_char[i])

            if list_char[i]=='[':
                count_left_bracket+=1
            elif list_char[i]==']':
                count_right_bracket+=1

            prev_type=cur_type

        list_str=(''.join(list_char2)).split('.')
        #list_str will be ['3', '[ab2[c]]', 'de', '44', '[f]']

        result=[]
        for i in range(len(list_str)):
            a_string=list_str[i]
            if char_type(a_string[0])==1:#letters
                result.append(a_string)
            elif char_type(a_string[0])==2:#left bracket
                pass
            elif char_type(a_string[0])==0:#number
                len_str=len(list_str[i+1])
                next_string=self.decodeString(list_str[i+1][1:len_str-1])
                repeat=int(a_string)
                for j in range(repeat):
                    result.append(next_string)

        result_str=''.join(result)
        return result_str



        
