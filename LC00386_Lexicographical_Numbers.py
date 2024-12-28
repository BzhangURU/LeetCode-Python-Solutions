# LC00386_Lexicographical_Numbers.py
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
    def get_num(self, cur_digits):
        number=0
        for i in range(len(cur_digits)):
            number=number*10+cur_digits[i]
        return number
    def get_result(self, n_digits, result, cur_digits, cur_tree_depth):
        if cur_tree_depth==0:
            for i in range(1,10):
                if i>n_digits[cur_tree_depth] and cur_tree_depth+1==len(n_digits):
                    break
                cur_digits.append(i)
                self.get_result(n_digits,result,cur_digits,cur_tree_depth+1)
                cur_digits.pop()
        else:
            result.append(self.get_num(cur_digits))
            if cur_tree_depth+1<=len(n_digits):
                for i in range(10):
                    if cur_tree_depth+1==len(n_digits):
                        cur_digits_num=self.get_num(cur_digits)
                        n_digits_num=self.get_num(n_digits)
                        if cur_digits_num*10+i>n_digits_num:
                            break
                    cur_digits.append(i)
                    self.get_result(n_digits,result,cur_digits,cur_tree_depth+1)
                    cur_digits.pop()

    def lexicalOrder(self, n: int) -> List[int]:
        
        #if n is 4346, then n_digits is [4,3,2,6]
        n_digits=[]
        num=n
        while num!=0:
            n_digits.append(num%10)
            num=int(num/10)
        n_digits.reverse()
        result=[]

        self.get_result(n_digits, result, [], 0)
        return result
    
my_solu=Solution()
print(my_solu.lexicalOrder(13))


        

