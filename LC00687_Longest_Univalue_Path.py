# LC00687_Longest_Univalue_Path.py

# Given the root of a binary tree, return the length of the longest path, 
# where each node in the path has the same value. This path may or may not pass through the root.

# The length of the path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [5,4,5,1,1,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value (i.e. 5).
# Example 2:


# Input: root = [1,4,5,4,4,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value (i.e. 4).
 

# Constraints:

# The number of nodes in the tree is in the range [0, 10**4].
# -1000 <= Node.val <= 1000
# The depth of the tree will not exceed 1000.

# Idea: for each node, get the longest single path that start from here and does down to descendents. 
# use post-order traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestOneWayPathFromHere(self, node, result_list): # return num nodes, while result_list saves length of path
        if node is None:
            return 0
        left_output=self.longestOneWayPathFromHere(node.left, result_list)
        right_output=self.longestOneWayPathFromHere(node.right, result_list)
        count_nodes_in_path=1
        num_extra_nodes_in_one_way_path=0
        if left_output>0 and node.left.val==node.val:
            count_nodes_in_path+=left_output
            num_extra_nodes_in_one_way_path=left_output
        if right_output>0 and node.right.val==node.val:
            count_nodes_in_path+=right_output
            if num_extra_nodes_in_one_way_path<right_output:
                num_extra_nodes_in_one_way_path=right_output
        if count_nodes_in_path-1>result_list[0]:
            result_list[0]=count_nodes_in_path-1
        
        
        return 1+num_extra_nodes_in_one_way_path

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        result_list=[0]
        self.longestOneWayPathFromHere(root, result_list)
        return result_list[0]

        

