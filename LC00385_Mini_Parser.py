# LC00385_Mini_Parser.py

# Given a string s represents the serialization of a nested list, 
# implement a parser to deserialize it and return the deserialized NestedInteger.

# Each element is either an integer or a list whose elements may also be 
# integers or other lists.

 

# Example 1:

# Input: s = "324"
# Output: 324
# Explanation: You should return a NestedInteger object which contains a single integer 324.
# Example 2:

# Input: s = "[123,[456,[789]]]"
# Output: [123,[456,[789]]]
# Explanation: Return a NestedInteger object containing a nested list with 2 elements:
# 1. An integer containing value 123.
# 2. A nested list containing two elements:
#     i.  An integer containing value 456.
#     ii. A nested list with one element:
#          a. An integer containing value 789
 

# Constraints:

# 1 <= s.length <= 5 * 104
# s consists of digits, square brackets "[]", negative sign '-', and commas ','.
# s is the serialization of valid NestedInteger.
# All the values in the input are in the range [-106, 106].

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s.find('[')<0:
            ele=NestedInteger(int(s))
            return ele
        elif s=='[]':
            return NestedInteger()
        else:
            #"[11,22,[1,2,4]]"
            s_length=len(s)
            #list_one_level will be ["11","22","[1,2,4]"]

            #to do it, we first change "[11,22,[1,2,4]]" to "[11a22a[1,2,4]]", then split based on 'a'
            s_list=list(s)
            count_left_bracket=0
            count_right_bracket=0
            for i in range(s_length):
                if s[i]=='[':
                    count_left_bracket+=1
                elif s[i]==']':
                    count_right_bracket+=1
                elif s[i]==',':
                    if count_left_bracket==count_right_bracket+1:
                        s_list[i]='a'
            s_string=''.join(s_list)
            s_string=s_string[1:s_length-1]
            list_one_level=s_string.split('a')

            result=NestedInteger()
            for i in range(len(list_one_level)):
                ele=self.deserialize(list_one_level[i])
                result.add(ele)
            return result





        
        
