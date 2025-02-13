# LC00424_Longest_Repeating_Character_Replacement.py

# You are given a string s and an integer k. You can choose any character 
# of the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you 
# can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 10**5
# s consists of only uppercase English letters.
# 0 <= k <= s.length

from collections import deque

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result=0
        my_q=deque()
        for letter_index in range(26):
            letter=chr(ord('A')+letter_index)
            # queue saves indexes(pos) of char that is not letter, queue's max size is k+1(we will pop out if size > k+1)
            my_q.clear()
            for i in range(len(s)):
                if s[i]!=letter:
                    my_q.append(i)
                    if len(my_q)>k+1:
                        my_q.popleft()
                left_boundary=-1

                if len(my_q)==k+1:
                    left_boundary=my_q[0]
                if i-left_boundary>result:
                    result=i-left_boundary
        return result

my_solu=Solution()
my_solu.characterReplacement("ABAB",2)

        
