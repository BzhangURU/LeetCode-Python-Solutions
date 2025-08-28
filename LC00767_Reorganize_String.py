# LC00767_Reorganize_String.py

# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

# Example 1:

# Input: s = "aab"
# Output: "aba"
# Example 2:

# Input: s = "aaab"
# Output: ""
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.

# Idea: to get string, always take letter with current max frequency, unless the last letter was it. In 
# that case take the letter with second max frequency. 


class Solution:
    def reorganizeString(self, s: str) -> str:
        dict_letter_freq={}
        max_freq=1
        for i in range(len(s)):
            if s[i] not in dict_letter_freq:
                dict_letter_freq[s[i]]=1
            else:

                dict_letter_freq[s[i]]+=1
                if dict_letter_freq[s[i]]>max_freq:
                    max_freq=dict_letter_freq[s[i]]
        if max_freq*2-1>len(s):
            return ""
        
        sorted_list=[]
        for k,v in dict_letter_freq.items():
            sorted_list.append([k,v])
        sorted_list.sort(key=lambda p:-p[1])#descending
        
        count=0
        output_list=[]
        while len(sorted_list)>0:
            if len(output_list)==0 or output_list[-1]!=sorted_list[0][0]:
                output_list.append(sorted_list[0][0])
                sorted_list[0][1]-=1
                if sorted_list[0][1]==0:
                    del sorted_list[0]
                sorted_list.sort(key=lambda p:-p[1])
            else:
                output_list.append(sorted_list[1][0])
                sorted_list[1][1]-=1
                if sorted_list[1][1]==0:
                    del sorted_list[1]
                sorted_list.sort(key=lambda p:-p[1])
        output="".join(output_list)
        return output
