##Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.
##
##Examples 1
##Input:
##
##  5
## /  \
##2   -3
##return [2, -3, 4], since all the values happen only once, return all of them in any order.
##Examples 2
##Input:
##
##  5
## /  \
##2   -5
##return [2], since 2 happens twice, however -5 only occur once.
##Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getSumOfTree(self, root, myList):
        if root.left == None and root.right == None:
            sum=0
        elif root.right == None:
            sum=self.getSumOfTree(root.left, myList)
        elif root.left == None:
            sum=self.getSumOfTree(root.right, myList)
        else:
            sum=self.getSumOfTree(root.left, myList)+\
                 self.getSumOfTree(root.right, myList)
        sum=sum+root.val
        myList.append(sum)
        return sum
    
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        sumList=[]
        result=[]
        if root==None:
            return sumList
        self.getSumOfTree(root, sumList)
        sumList.sort()
        maxFrequency=0
        curValue=sumList[0]
        curFre=0
        for i in range(len(sumList)):
            if sumList[i]==curValue:
                curFre+=1
            else:
                curValue=sumList[i]
                curFre=1
            if curFre>maxFrequency:
                    maxFrequency=curFre
        curValue=sumList[0]
        curFre=0
        for i in range(len(sumList)):
            if sumList[i]==curValue:
                curFre+=1
            else:
                curValue=sumList[i]
                curFre=1
            if curFre==maxFrequency:
                result.append(sumList[i])
        return result
