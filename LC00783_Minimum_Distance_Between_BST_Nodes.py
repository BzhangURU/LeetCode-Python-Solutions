# LC00783_Minimum_Distance_Between_BST_Nodes.py

# Given the root of a Binary Search Tree (BST), return the minimum difference 
# between the values of any two different nodes in the tree.

 

# Example 1:


# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:


# Input: root = [1,0,48,null,null,12,49]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 100].
# 0 <= Node.val <= 10**5

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Idea: traverse the tree, save all nums to list, then sort list, then get answer.


class Solution:
    def traverse_tree(self,node,nums):
        nums.append(node.val)
        if node.left!=None:
            self.traverse_tree(node.left,nums)
        if node.right!=None:
            self.traverse_tree(node.right,nums)
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nums=[]
        self.traverse_tree(root,nums)
        nums.sort()
        output=nums[1]-nums[0]
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1]<output:
                output=nums[i]-nums[i-1]
        return output


        
