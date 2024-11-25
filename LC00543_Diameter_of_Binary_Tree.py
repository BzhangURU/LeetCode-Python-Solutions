# LC00543_Diameter_of_Binary_Tree.py

# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#idea: post traversal, for each node, check left's longest path and right's longest path

class Solution:
    def traverse_tree(self, node, diameter):
        if node.left is None:
            longest_path_on_left=0
        else:
            longest_path_on_left=1+self.traverse_tree(node.left, diameter)
        if node.right is None:
            longest_path_on_right=0
        else:
            longest_path_on_right=1+self.traverse_tree(node.right, diameter)
        if longest_path_on_left+longest_path_on_right>diameter[0]:
            diameter[0]=longest_path_on_left+longest_path_on_right
        return max(longest_path_on_left,longest_path_on_right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=[0]
        self.traverse_tree(root, diameter)
        return diameter[0]
