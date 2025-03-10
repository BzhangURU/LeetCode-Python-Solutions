# LC00653_Two_Sum_IV-Input_is_a_BST_solution2.py

# Given the root of a binary search tree and an integer k, return true if 
# there exist two elements in the BST such that their sum is equal to k, 
# or false otherwise.

 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# Example 2:


# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 10**4].
# -10**4 <= Node.val <= 10**4
# root is guaranteed to be a valid binary search tree.
# -10**5 <= k <= 10**5

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Idea: map tree to sorted list, then do two sum

class Solution:
    def traverse_tree(self,node,sorted_list):
        if node is None:
            return
        self.traverse_tree(node.left,sorted_list)
        sorted_list.append(node.val)
        self.traverse_tree(node.right,sorted_list)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        sorted_list=[]
        self.traverse_tree(root,sorted_list)
        left=0
        right=len(sorted_list)-1

        for left in range(len(sorted_list)):
            if left>=right:
                break
            while sorted_list[left]+sorted_list[right]>k:
                right-=1
                if left>=right:
                    return False
            if sorted_list[left]+sorted_list[right]==k:
                return True
        return False

        


