

#LC00395_Longest_Substring_with_At_Least_K_Repeating_Characters.py

# Given a string s and an integer k, return the length of the longest 
# substring of s such that the frequency of each character in 
# this substring is greater than or equal to k.

# if no such substring exists, return 0.

 

# Example 1:

# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:

# Input: s = "ababbc", k = 2
# Output: 5
# Explanation: The longest substring is "ababb", as 'a' is repeated 2 times 
# and 'b' is repeated 3 times.
 

# Constraints:

# 1 <= s.length <= 10**4
# s consists of only lowercase English letters.
# 1 <= k <= 10**5

# Idea: first check freq of letters on s, if there is no letter freq<k, then that's it.
# Otherwise, all the letters with freq<k should not be included in the substring. 
# For example, b's freq<k, xxxxxbxxxxbxxxxbxxxxbxxxbxxxxxxxb, then we can only find substring between dif b.
# we use a freq_bin to track freq in all intervals. 

class Solution:
    def letter_index(self,char):
        return ord(char)-ord('a')
    def longestSubstring(self, s: str, k: int) -> int:
        freq_bin=[[0 for i in range(26)] for j in range(len(s)+1)]
        for i in range(1, len(s)+1):
            freq_bin[i][self.letter_index(s[i-1])]=1
            for j in range(26):
                freq_bin[i][j]+=freq_bin[i-1][j]
        
        set_bad_letters_index=set()
        for j in range(26):
            if freq_bin[len(s)][j]<k:
                set_bad_letters_index.add(j)

        result=0

        left=0
        
        #search
        for right in range(len(s)+1):
            if right==5:
                right=right
            if right==len(s) or self.letter_index(s[right]) in set_bad_letters_index:
                find_one_candidate=True
                find_possible=False#s="bbaaacbd"
                for j in range(26):
                    letter_freq=freq_bin[right][j]-freq_bin[left][j]
                    if letter_freq>0 and letter_freq<k:
                        find_one_candidate=False
                    if letter_freq>=k:
                        find_possible=True
                if find_one_candidate and right-left>result:
                    result=right-left
                elif find_possible:
                    substring_result=self.longestSubstring(s[left:right],k)
                    if substring_result>result:
                        result=substring_result
                left=right+1
        #print(result)
        return result


my_solu=Solution()
k=3
s="bbaaacbd"
my_solu.longestSubstring(s,k)



