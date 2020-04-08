##530. Minimum Absolute Difference in BST
##Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
##
##Example:
##
##Input:
##
##   1
##    \
##     3
##    /
##   2
##
##Output:
##1
##
##Explanation:
##The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
## 
##
##Note:
##
##There are at least two nodes in this BST.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        list=[]
        def searchTree(list, root: TreeNode):
            if root.left!=None:
                searchTree(list, root.left)
            list.append(root.val)
            if root.right!=None:
                searchTree(list, root.right)
            
        searchTree(list, root)
        return min(list[i+1]-list[i] for i in range(len(list)-1))
