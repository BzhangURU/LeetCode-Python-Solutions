# LC00676_Implement_Magic_Dictionary.py

# Design a data structure that is initialized with a list of different words. 
# Provided a string, you should determine if you can change exactly one character 
# in this string to match any word in the data structure.

# Implement the MagicDictionary class:

# MagicDictionary() Initializes the object.
# void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.
# bool search(String searchWord) Returns true if you can change exactly one character in 
# searchWord to match any string in the data structure, otherwise returns false.
 

# Example 1:

# Input
# ["MagicDictionary", "buildDict", "search", "search", "search", "search"]
# [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
# Output
# [null, null, false, true, false, false]

# Explanation
# MagicDictionary magicDictionary = new MagicDictionary();
# magicDictionary.buildDict(["hello", "leetcode"]);
# magicDictionary.search("hello"); // return False
# magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to match "hello" so we return True
# magicDictionary.search("hell"); // return False
# magicDictionary.search("leetcoded"); // return False
 

# Constraints:

# 1 <= dictionary.length <= 100
# 1 <= dictionary[i].length <= 100
# dictionary[i] consists of only lower-case English letters.
# All the strings in dictionary are distinct.
# 1 <= searchWord.length <= 100
# searchWord consists of only lower-case English letters.
# buildDict will be called only once before search.
# At most 100 calls will be made to search.

# Idea: if a word is hello, use dictionary to save {*ello:h, h*llo:e, ...}
# the value means the letter that can't be used to replace *. If there is another word 
# like eello, then *ello:h is changed to *ello:*


class MagicDictionary:
    def __init__(self):
        self.my_dict={}
        
    def buildDict(self, dictionary: List[str]) -> None:
        for i in range(len(dictionary)):
            cur_str=dictionary[i]
            str_list=list(cur_str)
            for j in range(len(str_list)):
                cur_char=str_list[j]
                str_list[j]='*'
                replaced_str=''.join(str_list)
                if replaced_str not in self.my_dict:
                    self.my_dict[replaced_str]=cur_char
                elif self.my_dict[replaced_str]!=cur_char:
                    self.my_dict[replaced_str]='*'
                str_list[j]=cur_char

    def search(self, searchWord: str) -> bool:
        str_list=list(searchWord)
        for j in range(len(str_list)):
            cur_char=str_list[j]
            str_list[j]='*'
            replaced_str=''.join(str_list)
            if replaced_str in self.my_dict and self.my_dict[replaced_str]!=cur_char:
                return True
            str_list[j]=cur_char
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
