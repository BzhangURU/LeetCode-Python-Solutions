# LC00591_Tag_Validator.py

# Given a string representing a code snippet, implement a tag validator to parse the code and return whether it is valid.

# A code snippet is valid if all the following rules hold:

# The code must be wrapped in a valid closed tag. Otherwise, the code is invalid.
# A closed tag (not necessarily valid) has exactly the following format : <TAG_NAME>TAG_CONTENT</TAG_NAME>. 
# Among them, <TAG_NAME> is the start tag, and </TAG_NAME> is the end tag. The TAG_NAME in start 
# and end tags should be the same. A closed tag is valid if and only if the TAG_NAME and TAG_CONTENT are valid.
# A valid TAG_NAME only contain upper-case letters, and has length in range [1,9]. Otherwise, the TAG_NAME is invalid.
# A valid TAG_CONTENT may contain other valid closed tags, cdata and any characters (see note1) EXCEPT unmatched <, 
# unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the TAG_CONTENT is invalid.
# A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to 
# consider the issue of unbalanced when tags are nested.
# A < is unmatched if you cannot find a subsequent >. And when you find a < or </, all the subsequent characters 
# until the next > should be parsed as TAG_NAME (not necessarily valid).
# The cdata has the following format : <![CDATA[CDATA_CONTENT]]>. The range of CDATA_CONTENT is defined as the 
# characters between <![CDATA[ and the first subsequent ]]>.
# CDATA_CONTENT may contain any characters. The function of cdata is to forbid the validator to parse CDATA_CONTENT, 
# so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it 
# as regular characters.
 

# Example 1:

# Input: code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
# Output: true
# Explanation: 
# The code is wrapped in a closed tag : <DIV> and </DIV>. 
# The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata. 
# Although CDATA_CONTENT has an unmatched start tag with invalid TAG_NAME, 
# it should be considered as plain text, not parsed as a tag.
# So TAG_CONTENT is valid, and then the code is valid. Thus return true.
# Example 2:

# Input: code = "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"
# Output: true
# Explanation:
# We first separate the code into : start_tag|tag_content|end_tag.
# start_tag -> "<DIV>"
# end_tag -> "</DIV>"
# tag_content could also be separated into : text1|cdata|text2.
# text1 -> ">>  ![cdata[]] "
# cdata -> "<![CDATA[<div>]>]]>", where the CDATA_CONTENT is "<div>]>"
# text2 -> "]]>>]"
# The reason why start_tag is NOT "<DIV>>>" is because of the rule 6.
# The reason why cdata is NOT "<![CDATA[<div>]>]]>]]>" is because of the rule 7.
# Example 3:

# Input: code = "<A>  <B> </A>   </B>"
# Output: false
# Explanation: Unbalanced. If "<A>" is closed, then "<B>" must be unmatched, and vice versa.
 

# Constraints:

# 1 <= code.length <= 500
# code consists of English letters, digits, '<', '>', '/', '!', '[', ']', '.', and ' '.

from collections import deque
def get_tag_type_and_tag_name_and_right_arrow_ind(code, left_arrow_ind):
    # we run this function when code[left_arrow_ind] is '<'

    # start tag: 0, end tag: 1, CDATA tag: 2, invalid tag: 3
    # also verify the correctness of tag

    # first verify if it is <![CDATA[
    if left_arrow_ind>=len(code)-1:
        #invalid tag
        return 3,'1',-1
    elif code[left_arrow_ind+1]=='!':
        # if it may be CDATA tag
        if left_arrow_ind+len('<![CDATA[')>=len(code)-1:
            return 3,'2',-1
        elif code[left_arrow_ind:left_arrow_ind+len('<![CDATA[')]!='<![CDATA[':
            return 3,'3',-1
        find_CDATA_end_ind=code[left_arrow_ind:].find(']]>')+left_arrow_ind
        if find_CDATA_end_ind<0:
            return 3,'4',-1
        else:
            right_arrow_ind=find_CDATA_end_ind+2
            return 2,'',right_arrow_ind
    elif code[left_arrow_ind+1]=='/':
        #end tag
        right_arrow_ind=code[left_arrow_ind:].find('>')+left_arrow_ind
        if right_arrow_ind<0:
            return 3,'5',-1
        #verify only upper case letters exist between left and right, and length 1-9
        # </A>
        if right_arrow_ind-left_arrow_ind>=12 or right_arrow_ind-left_arrow_ind<=2:
            return 3,'6',-1
        for i in range(left_arrow_ind+2,right_arrow_ind):
            if ord(code[i])<ord('A') or ord(code[i])>ord('Z'):
                return 3,'7',-1
        return 1,code[left_arrow_ind+2:right_arrow_ind],right_arrow_ind
    else:
        #start tag
        right_arrow_ind=code[left_arrow_ind:].find('>')+left_arrow_ind
        if right_arrow_ind<0:
            return 3,'8',-1
        # <A>
        if right_arrow_ind-left_arrow_ind>=11 or right_arrow_ind-left_arrow_ind<=1:
            return 3,'9',-1
        for i in range(left_arrow_ind+1,right_arrow_ind):
            if ord(code[i])<ord('A') or ord(code[i])>ord('Z'):
                return 3,'10',-1
        return 0,code[left_arrow_ind+1:right_arrow_ind],right_arrow_ind
        



class Solution:
    def isValid(self, code: str) -> bool:
        tag_stack=deque()
        i=0
        while i<len(code):
            if i>0 and len(tag_stack)==0:
                return False
            if code[i]!='<':
                # It is content
                if len(tag_stack)==0:
                    return False
            else:
                # left arrow
                tag_type, tag_name, right_arrow_ind=get_tag_type_and_tag_name_and_right_arrow_ind(code, i)
                if tag_type==3:
                    return False
                elif tag_type==2:
                    i=right_arrow_ind
                    if len(tag_stack)==0:
                        return False
                elif tag_type==1:
                    #verify end_tag matches with top element in stack
                    if len(tag_stack)==0 or tag_name!=tag_stack[-1]:
                        return False
                    else:
                        tag_stack.pop()
                        i=right_arrow_ind
                else:
                    # tag_type==0:
                    tag_stack.append(tag_name)
                    i=right_arrow_ind
            i+=1

        if len(tag_stack)>0:
            return False
        return True


my_solu=Solution()
my_solu.isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV>")



