# LC00653_Two_Sum_IV-Input_is_a_BST.py

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
class Solution:
    # find if target num exist in tree
    def find_num(self, node, num):
        if node.val==num:
            return True
        elif num<node.val:
            if node.left is None:
                return False
            else:
                return self.find_num(node.left, num)
        elif node.val<num:
            if node.right is None:
                return False
            else:
                return self.find_num(node.right, num)
    def traverse_tree(self,node,root,k):
        cur_val=node.val
        if self.find_num(root,k-cur_val) and 2*cur_val!=k:
            return True
        else:
            answer=False
            if node.left is not None:
                if self.traverse_tree(node.left,root,k):
                    answer=True
            if node.right is not None and answer==False:
                if self.traverse_tree(node.right,root,k):
                    answer=True
            return answer



    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.traverse_tree(root,root,k)

        


