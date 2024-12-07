# LC00572_Subtree_of_Another_Tree.py

# Given the roots of two binary trees root and subRoot, return true if there is 
# a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and 
# all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

# Example 1:


# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:


# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
 

# Constraints:

# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -10^4 <= root.val <= 10^4
# -10^4 <= subRoot.val <= 10^4

#Idea: first check the depth of each node in tree, only start from the node that
# has the same depth with the subtree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth_of_node(self, node):
        if node is None:
            return 0
        left_depth=self.depth_of_node(node.left)
        right_depth=self.depth_of_node(node.right)
        return max(left_depth, right_depth)+1

    def two_trees_are_same(self, node, subNode):
        if node is None and subNode is None:
            return True
        if node is None and subNode is not None:
            return False
        if node is not None and subNode is None:
            return False
        if node.val!=subNode.val:
            return False
        left_same=self.two_trees_are_same(node.left, subNode.left)
        if left_same==False:
            return False
        right_same=self.two_trees_are_same(node.right, subNode.right)
        if right_same==False:
            return False
        return True

    def traverse_node_depth(self, node, subRoot, depth_goal, result):
        if node is None:
            return 0
        left_depth=self.traverse_node_depth(node.left, subRoot, depth_goal, result)
        if result[0]:
            #already found same tree, stop program
            return -1
        right_depth=self.traverse_node_depth(node.right, subRoot, depth_goal, result)
        if result[0]:
            #already found same tree, stop program
            return -1

        current_depth=max(left_depth, right_depth)+1
        if current_depth==depth_goal:
            if self.two_trees_are_same(node, subRoot):
                result[0]=True

        return current_depth
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        result=[False]
        depth_goal=self.depth_of_node(subRoot)
        self.traverse_node_depth(root, subRoot, depth_goal, result)
        return result[0]
        


        
