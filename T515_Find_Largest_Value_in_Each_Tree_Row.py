#https://leetcode.com/problems/find-largest-value-in-each-tree-row/
##You need to find the largest value in each row of a binary tree.
##
##Example:
##Input: 
##
##          1
##         / \
##        3   2
##       / \   \  
##      5   3   9 
##
##Output: [1, 3, 9]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverseToFindLargest(self, node, mylist, layer):
        if len(mylist)<=layer:
            mylist.append(node.val)
        elif mylist[layer]<node.val:
            mylist[layer]=node.val
        if node.left!=None:
            self.traverseToFindLargest(node.left, mylist, layer+1)
        if node.right!=None:
            self.traverseToFindLargest(node.right, mylist, layer+1)
    def largestValues(self, root: TreeNode) -> List[int]:
        mylist=[]
        if root!=None:
            self.traverseToFindLargest(root, mylist, 0)
        return mylist
