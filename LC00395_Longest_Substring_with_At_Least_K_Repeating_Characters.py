

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
