# LC00386_Lexicographical_Numbers_faster.py
# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

# You must write an algorithm that runs in O(n) time and uses O(1) extra space. 


# Example 1:

# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
# Example 2:

# Input: n = 2
# Output: [1,2]
 

# Constraints:

# 1 <= n <= 5 * 10**4

#Idea: Trie-tree. split into digits.
from typing import List
class Solution:
    def get_result(self, n, result, cur_str):
        if len(cur_str)==0:
            for i in range(1,10):
                if i>n:
                    break
                self.get_result(n,result,cur_str+str(i))
        else:
            result.append(int(cur_str))
            if len(cur_str)<len(str(n)):
                for i in range(10):
                    if len(cur_str)+1==len(str(n)):
                        if int(cur_str)*10+i>n:
                            break
                    self.get_result(n,result,cur_str+str(i))

    def lexicalOrder(self, n: int) -> List[int]:
        result=[]
        self.get_result(n, result, "")
        return result
    
my_solu=Solution()
print(my_solu.lexicalOrder(13))


        

