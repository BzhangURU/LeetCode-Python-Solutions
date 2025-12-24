

# LC00814_Binary_Tree_Pruning.py

# Given the root of a binary tree, return the same tree where every subtree (of the given tree) 
# not containing a 1 has been removed.

# A subtree of a node node is node plus every node that is a descendant of node.

 

# Example 1:


# Input: root = [1,null,0,0,1]
# Output: [1,null,0,null,1]
# Explanation: 
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.
# Example 2:


# Input: root = [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]
# Example 3:


# Input: root = [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 200].
# Node.val is either 0 or 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def my_prune_tree(self,node):
        sum_left=0
        sum_right=0
        if node.left is not None:
            sum_left=self.my_prune_tree(node.left)
            if sum_left==0:
                node.left=None
        if node.right is not None:
            sum_right=self.my_prune_tree(node.right)
            if sum_right==0:
                node.right=None
        return sum_left+sum_right+node.val
        
        

    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.my_prune_tree(root)
        if root.left is None and root.right is None and root.val==0:
            return None
        return root
        


