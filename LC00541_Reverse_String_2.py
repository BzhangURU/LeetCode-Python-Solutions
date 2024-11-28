# LC00541_Reverse_String_2.py

# Given a string s and an integer k, reverse the first k characters for every 2k 
# characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If there are less 
# than 2k but greater than or equal to k characters, then reverse the first k characters 
# and leave the other as original.

 

# Example 1:

# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:

# Input: s = "abcd", k = 2
# Output: "bacd"
 

# Constraints:

# 1 <= s.length <= 10^4
# s consists of only lowercase English letters.
# 1 <= k <= 10^4

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        str_list=list(s)

        num_chunk=len(str_list)//(2*k)
        num_remaining=len(str_list)%(2*k)

        for chunk_ind in range(num_chunk):
            reversed_string_list_in_a_chunk=str_list[chunk_ind*2*k:chunk_ind*2*k+k]
            reversed_string_list_in_a_chunk.reverse()
            str_list[chunk_ind*2*k:chunk_ind*2*k+k]=reversed_string_list_in_a_chunk
        if num_remaining >= k:
            reversed_string_list_in_a_chunk=str_list[num_chunk*2*k:num_chunk*2*k+k]
            reversed_string_list_in_a_chunk.reverse()
            str_list[num_chunk*2*k:num_chunk*2*k+k]=reversed_string_list_in_a_chunk
        else:
            reversed_string_list_in_a_chunk=str_list[num_chunk*2*k:num_chunk*2*k+num_remaining]
            reversed_string_list_in_a_chunk.reverse()
            str_list[num_chunk*2*k:num_chunk*2*k+num_remaining]=reversed_string_list_in_a_chunk


        answer=''.join(str_list)
        return answer
