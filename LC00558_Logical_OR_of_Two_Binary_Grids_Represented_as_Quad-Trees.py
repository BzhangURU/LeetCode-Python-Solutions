# LC00558_Logical_OR_of_Two_Binary_Grids_Represented_as_Quad-Trees.py

# A Binary Matrix is a matrix in which all the elements are either 0 or 1.

# Given quadTree1 and quadTree2. quadTree1 represents a n * n binary matrix and quadTree2 represents another n * n binary matrix.

# Return a Quad-Tree representing the n * n binary matrix which is the result of logical bitwise OR of the two binary matrixes represented by quadTree1 and quadTree2.

# Notice that you can assign the value of a node to True or False when isLeaf is False, and both are accepted in the answer.

# A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

# val: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
# isLeaf: True if the node is leaf node on the tree or False if the node has the four children.
# class Node {
#     public boolean val;
#     public boolean isLeaf;
#     public Node topLeft;
#     public Node topRight;
#     public Node bottomLeft;
#     public Node bottomRight;
# }
# We can construct a Quad-Tree from a two-dimensional area using the following steps:

# If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
# If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
# Recurse for each of the children with the proper sub-grid.

# If you want to know more about the Quad-Tree, you can refer to the wiki.

# Quad-Tree format:

# The input/output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.

# It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].

# If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.

 

# Example 1:


# Input: quadTree1 = [[0,1],[1,1],[1,1],[1,0],[1,0]]
# , quadTree2 = [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
# Output: [[0,0],[1,1],[1,1],[1,1],[1,0]]
# Explanation: quadTree1 and quadTree2 are shown above. You can see the binary matrix which is represented by each Quad-Tree.
# If we apply logical bitwise OR on the two binary matrices we get the binary matrix below which is represented by the result Quad-Tree.
# Notice that the binary matrices shown are only for illustration, you don't have to construct the binary matrix to get the result tree.

# Example 2:

# Input: quadTree1 = [[1,0]], quadTree2 = [[1,0]]
# Output: [[1,0]]
# Explanation: Each tree represents a binary matrix of size 1*1. Each matrix contains only zero.
# The resulting matrix is of size 1*1 with also zero.
 

# Constraints:

# quadTree1 and quadTree2 are both valid Quad-Trees each representing a n * n grid.
# n == 2^x where 0 <= x <= 9.

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

#Idea: we traverse tree to perform OR, in the meantime, we check if we can merge(delete children because all children have same value now)

class Solution:
    def traverse_2_trees_to_merge_OR(self, node1, node2):
        # calculate OR operation and save it to node1
        #if node1 | node2 is always 0 or always 1, return 0 or 1, otherwise return -1 


        if node1.isLeaf and node2.isLeaf:
            node1.val=node1.val | node2.val
            if node1.val:
                return 1
            else:
                return 0
        elif node1.isLeaf:#node 1 leaf, node 2 not leaf
            if node1.val:
                #1 | x is always 1
                return 1
            else:
                
                #0 | x is always x
                #copy node2 to node1
                node1.isLeaf=False
                node1.topLeft=node2.topLeft
                node1.topRight=node2.topRight
                node1.bottomLeft=node2.bottomLeft
                node1.bottomRight=node2.bottomRight
                #node2 is from a qualified quad-tree's node, we can't merge
                return -1
                
        elif node2.isLeaf:#node 1 not leaf, node 2 leaf
            if node2.val:
                #1 | x is always 1
                node1.val=True
                node1.isLeaf=True
                node1.topLeft=None
                node1.topRight=None
                node1.bottomLeft=None
                node1.bottomRight=None
                return 1
            else:
                #0 | x is always x
                #node1 is from a qualified quad-tree's node, we can't merge
                return -1
        else:
            #both not leaf
            v1=self.traverse_2_trees_to_merge_OR(node1.topLeft, node2.topLeft)
            v2=self.traverse_2_trees_to_merge_OR(node1.topRight, node2.topRight)
            v3=self.traverse_2_trees_to_merge_OR(node1.bottomLeft, node2.bottomLeft)
            v4=self.traverse_2_trees_to_merge_OR(node1.bottomRight, node2.bottomRight)

            if v1==v2 and v2==v3 and v3==v4:
                if v1==1:
                    #all 1, can merge
                    node1.val=True
                    node1.isLeaf=True
                    node1.topLeft=None
                    node1.topRight=None
                    node1.bottomLeft=None
                    node1.bottomRight=None
                    return 1
                elif v1==0:
                    #all 0, can merge
                    node1.val=False
                    node1.isLeaf=True
                    node1.topLeft=None
                    node1.topRight=None
                    node1.bottomLeft=None
                    node1.bottomRight=None
                    return 0
                else:
                    return -1
            else:
                return -1


    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        self.traverse_2_trees_to_merge_OR(quadTree1,quadTree2)
        return quadTree1
        

