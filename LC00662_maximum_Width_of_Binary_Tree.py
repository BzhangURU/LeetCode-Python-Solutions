# LC00662_maximum_Width_of_Binary_Tree.py

# Given the root of a binary tree, return the maximum width of the given tree.

# The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

# It is guaranteed that the answer will in the range of a 32-bit signed integer.

 

# Example 1:


# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
# Example 2:


# Input: root = [1,3,2,5,null,null,9,6,null,7]
# Output: 7
# Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
# Example 3:


# Input: root = [1,3,2,5]
# Output: 2
# Explanation: The maximum width exists in the second level with length 2 (3,2).
 

# Constraints:

# The number of nodes in the tree is in the range [1, 3000].
# -100 <= Node.val <= 100

# Idea: use BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    #def searchTree(self, root):
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        my_q=deque()
        my_q.append([root, 0])
        result=0
        while my_q:
            count_node_in_cur_layer=len(my_q)
            left_most=-1
            right_most=-1
            for i in range(count_node_in_cur_layer):
                node_ind=my_q.popleft()
                if left_most==-1:
                    left_most=node_ind[1]
                right_most=node_ind[1]
                if node_ind[0].left is not None:
                    my_q.append([node_ind[0].left, node_ind[1]*2])
                if node_ind[0].right is not None:
                    my_q.append([node_ind[0].right, node_ind[1]*2+1])
                if left_most!=-1 and right_most-left_most+1>result:
                    result=right_most-left_most+1
        return result


                


        
