##Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.
##
##A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.
##
##The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.
##
##Example 1:
##Input: "aba", "cdc", "eae"
##Output: 3
##Note:
##
##All the given strings' lengths will not exceed 10.
##The length of the given list will be in the range of [2, 50].

##My comments: if subsequence of string a is LUS, then a must be LUS. So we
## sort strings, and find the longest LUS. ##def findLUSlength(strs: List[str]) -> int:

import functools

class Solution:
    def cmpStr(self, a, b):
        if len(a)!=len(b):
            return len(b)-len(a)
        else:
            for i in range(len(a)):
                if a[i]!=b[i]:
                    return ord(a[i])-ord(b[i])
            return 0
    def isSubsequence(self, a, b):
        if len(a)>len(b):
            return False
        else:
            j=0
            for i in range(len(a)):
                while a[i]!=b[j]:
                    j=j+1
                    if j>=len(b) or len(a)-i>len(b)-j:
                        return False
                j=j+1
            return True
    #Check if string a is subsequence of b
    def findLUSlength(self, strs: List[str]) -> int:
        strs2=sorted(strs, key=functools.cmp_to_key(self.cmpStr))
        for i in range(len(strs2)):
            isLUS=True
            if i<len(strs2)-1:
                if strs2[i]==strs2[i+1]:
                    continue
            for j in range(i):
                if self.isSubsequence(strs2[i], strs2[j]):
                    isLUS=False
                    break
            if isLUS:
                return len(strs2[i])
        return -1
