# LC00421_Maximum_XOR_of_Two_Numbers_in_an_Array.py

# Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

 

# Example 1:

# Input: nums = [3,10,5,25,2,8]
# Output: 28
# Explanation: The maximum result is 5 XOR 25 = 28.
# Example 2:

# Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127
 

# Constraints:

# 1 <= nums.length <= 2 * 10**5
# 0 <= nums[i] <= 2**31 - 1

# Idea: sort in descending order, then build a Trie tree, higher bit is closer to root
# when we scan a num (101001), then we search (1(depth1)-->0(depth2)-->1-->1-->0), 
# if 0 doesn't exist in depth 2, then we go to 1 in depth 2, then keep searching 
from typing import List
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def add_a_leaf_to_tree(root, num):
    my_list=[0]*31
    for bit_pos in range(30,-1,-1):
        my_list[30-bit_pos]=(num>>bit_pos)&1

    node=root
    for i, bit in enumerate(my_list):
        if bit==0:
            if node.left is None:
                if i==len(my_list)-1:
                    new_node=TreeNode(num)
                else:
                    new_node=TreeNode(-1)
                node.left=new_node
            node=node.left
        else:
            if node.right is None:
                if i==len(my_list)-1:
                    new_node=TreeNode(num)
                else:
                    new_node=TreeNode(-1)
                node.right=new_node
            node=node.right

def find_num_closest_to_XOR_goal(root,XOR_goal):
    my_list=[0]*31
    for bit_pos in range(30,-1,-1):
        my_list[30-bit_pos]=(XOR_goal>>bit_pos)&1

    node=root

    for i, bit in enumerate(my_list):
        if bit==0:
            if node.left is not None:
                node=node.left
            else:
                node=node.right
        else:
            if node.right is not None:
                node=node.right
            else:
                node=node.left

    return node.val



class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        #nums.reverse()
        print(nums)

        root=TreeNode(-1)
        for i, num in enumerate(nums):
            add_a_leaf_to_tree(root,num)

        highest_bit_pos=0

        for i in range(31):
            if (nums[0]>>i)==1:
                highest_bit_pos=i
        print('highest_bit_pos:', highest_bit_pos)
        result=0

        for i,num in enumerate(nums):
            if (num>>highest_bit_pos)==0:
                break

            XOR_goal=(num ^ (2**(highest_bit_pos+1)-1))
            print(num, XOR_goal)

            partner=find_num_closest_to_XOR_goal(root,XOR_goal)
            print(num, partner)

            if num ^ partner>result:
                result=num ^ partner
        return result
    
my_solu=Solution()
my_solu.findMaximumXOR([3,10,5,25,2,8])





        
