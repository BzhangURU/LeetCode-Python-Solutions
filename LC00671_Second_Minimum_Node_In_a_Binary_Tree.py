# LC00671_Second_Minimum_Node_In_a_Binary_Tree.py

# Given a non-empty special binary tree consisting of nodes with the non-negative value, 
# where each node in this tree has exactly two or zero sub-node. If the node has two 
# sub-nodes, then this node's value is the smaller value among its two sub-nodes. More '
# 'formally, the property root.val = min(root.left.val, root.right.val) always holds.

# Given such a binary tree, you need to output the second minimum value in the set made 
# of all the nodes' value in the whole tree.

# If no such second minimum value exists, output -1 instead.

 

 

# Example 1:


# Input: root = [2,2,5,null,null,5,7]
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
# Example 2:


# Input: root = [2,2,2]
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest value.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 25].
# 1 <= Node.val <= 2**31 - 1
# root.val == min(root.left.val, root.right.val) for each internal node of the tree.
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Idea: min is at root

class Solution:
    def find_min_larger_than(self, thresh, node):
        if node.val>thresh:
            return node.val
        if node.left is not None and node.right is not None:
            left_result=self.find_min_larger_than(thresh,node.left)
            right_result=self.find_min_larger_than(thresh,node.right)
            if left_result>=0 and right_result>=0:
                return min(left_result,right_result)
            elif left_result>=0:
                return left_result
            elif right_result>=0:
                return right_result
            else:
                return -1
        return -1
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        return self.find_min_larger_than(root.val, root)
        

