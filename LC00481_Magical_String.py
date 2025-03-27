# LC00481_Magical_String.py

# A magical string s consists of only '1' and '2' and obeys the following rules:

# The string s is magical because concatenating the number of contiguous occurrences 
# of characters '1' and '2' generates the string s itself.
# The first few elements of s is s = "1221121221221121122……". If we group the consecutive 
# 1's and 2's in s, it will be "1 22 11 2 1 22 1 22 11 2 11 22 ......" and the occurrences 
# of 1's or 2's in each group are "1 2 2 1 1 2 1 2 2 1 2 2 ......". You can see that the 
# occurrence sequence is s itself.

# Given an integer n, return the number of 1's in the first n number in the magical string s.

 

# Example 1:

# Input: n = 6
# Output: 3
# Explanation: The first 6 elements of magical string s is "122112" and it contains three 1's, so return 3.
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 10**5

# Idea: keep generating array until n.

class Solution:
    def magicalString(self, n: int) -> int:
        list_a=[1,2,2,1,1,2,1,2,2,1,2,2,1,1,2,1,1,2,2]
        list_b=[1,2,2,1,1,2,1,2,2,1,2,2,1,1,2,1,1,2,2]

        #mapping_b_index_to_a=[0,2,4,5,6,8,9,11,13,14,16,18] # ,19,20,22,23,24,26,28]

        if n<=len(list_a):
            return list_a[:n].count(1)

        b_index_that_maps_the_end_of_a=11

        while True:
            if len(list_a)==len(list_b):
                #extend a

                start_b_index=b_index_that_maps_the_end_of_a+1
                length_b=len(list_b)
                for i in range(start_b_index,length_b):
                    if list_b[i]==1:
                        if list_a[-1]==1:
                            list_a.append(2)
                        else:
                            list_a.append(1)
                    else:
                        if list_a[-1]==1:
                            list_a.append(2)
                            list_a.append(2)
                        else:
                            list_a.append(1)
                            list_a.append(1)
                
                    if len(list_a)>=n:
                        return list_a[:n].count(1)
                b_index_that_maps_the_end_of_a=len(list_b)-1
            else:
                #extend b to copy a's results to b
                list_a_extra=list_a[len(list_b):len(list_a)]
                list_b.extend(list_a_extra)



        
