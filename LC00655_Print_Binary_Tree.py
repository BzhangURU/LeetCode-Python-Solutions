# LC00655_Print_Binary_Tree.py

# Given the root of a binary tree, construct a 0-indexed m x n string matrix res that 
# represents a formatted layout of the tree. The formatted layout matrix should be 
# constructed using the following rules:

# The height of the tree is height and the number of rows m should be equal to height + 1.
# The number of columns n should be equal to 2^(height+1) - 1.
# Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
# For each node that has been placed in the matrix at position res[r][c], place its 
# left child at res[r+1][c-2^(height-r)-1] and its right child at res[r+1][c+2^(height-r)-1].
# Continue this process until all the nodes in the tree have been placed.
# Any empty cells should contain the empty string "".
# Return the constructed matrix res.

 

# Example 1:


# Input: root = [1,2]
# Output: 
# [["","1",""],
#  ["2","",""]]
# Example 2:


# Input: root = [1,2,3,null,4]
# Output: 
# [["","","","1","","",""],
#  ["","2","","","","3",""],
#  ["","","4","","","",""]]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 210].
# -99 <= Node.val <= 99
# The depth of the tree will be in the range [1, 10].


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse_tree(self, node, row, col, tree_height, matrix):
        if node is not None:
            matrix[row][col]=str(node.val)
            self.traverse_tree(node.left, row+1, col-2**(tree_height-row-1), tree_height, matrix)
            self.traverse_tree(node.right, row+1, col+2**(tree_height-row-1), tree_height, matrix)


    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_tree_height(node):
            if node is None:
                return -1
            max_child_height=-1
            left_height=get_tree_height(node.left)
            right_height=get_tree_height(node.right)
            if left_height>right_height:
                max_child_height=left_height
            else:
                max_child_height=right_height

            return max_child_height+1
        
        tree_height=get_tree_height(root)

        matrix=[["" for _ in range(2**(tree_height+1)-1)] for _ in range(tree_height+1)]
        self.traverse_tree(root, 0, int((2**(tree_height+1)-1-1)/2), tree_height, matrix)

        return matrix


        

