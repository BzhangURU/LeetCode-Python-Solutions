##Given a binary tree, find the leftmost value in the last row of the tree.
##
##Example 1:
##Input:
##
##    2
##   / \
##  1   3
##
##Output:
##1
##Example 2:
##Input:
##
##        1
##       / \
##      2   3
##     /   / \
##    4   5   6
##       /
##      7
##
##Output:
##7
##Note: You may assume the tree (i.e., the given root node) is not NULL.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q=collections.deque()
        q.append(root)
        result=root.val
        while len(q)>0:
            result=q[0]
            num=len(q)
            for i in range(num):
                node=q.popleft()
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
        return result.val
