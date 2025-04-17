# LC00686_Repeated_String_Match.py

# Given two strings a and b, return the minimum number of times you should 
# repeat string a so that string b is a substring of it. If it is impossible 
# for b​​​​​​ to be a substring of a after repeating it, return -1.

# Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and 
# repeated 2 times is "abcabc".

 

# Example 1:

# Input: a = "abcd", b = "cdabcdab"
# Output: 3
# Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.
# Example 2:

# Input: a = "a", b = "aa"
# Output: 2
 

# Constraints:

# 1 <= a.length, b.length <= 10**4
# a and b consist of lowercase English letters.

# idea: first match the first letter of b to a char in a

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        for a_ind in range(len(a)):
            if a[a_ind]==b[0]:
                #keep comparing
                cur_result=True
                for b_ind in range(1,len(b)):
                    if b[b_ind]!=a[(a_ind+b_ind)%len(a)]:
                        cur_result=False
                        break
                if cur_result:
                    if a_ind+len(b)-1<len(a):
                        return 1
                    else:
                        return 1+(len(b)-1+a_ind)//len(a)#1+((len(b)-(len(a)-a_ind))+len(a)-1)//len(a)
        return -1
        
a="abcd"
b="cdabcdab"
my_solu=Solution()
my_solu.repeatedStringMatch(a,b)

