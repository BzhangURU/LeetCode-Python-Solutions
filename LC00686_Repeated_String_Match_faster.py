# LC00686_Repeated_String_Match_faster.py

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

# idea: Using find function is O(m+n)

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        len_repeated_a=len(a)+len(b)-1
        repeated_a_list=list(a)
        for i in range(len(a), len_repeated_a):
            repeated_a_list.append(a[i%len(a)])
        repeated_a=''.join(repeated_a_list)
        result=repeated_a.find(b)
        if result>=0:
            if result+len(b)-1<len(a):
                return 1
            else:
                return 1+(len(b)-1+result)//len(a)
        else:
            return -1


        
a="abcd"
b="cdabcdab"
my_solu=Solution()
my_solu.repeatedStringMatch(a,b)

