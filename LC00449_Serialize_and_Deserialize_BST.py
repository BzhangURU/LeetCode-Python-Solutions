# LC00449_Serialize_and_Deserialize_BST.py

# Serialization is converting a data structure or object into a sequence of bits so 
# that it can be stored in a file or memory buffer, or transmitted across a network 
# connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree. There is no 
# restriction on how your serialization/deserialization algorithm should work. 
# You need to ensure that a binary search tree can be serialized to a string, and 
# this string can be deserialized to the original tree structure.

# The encoded string should be as compact as possible.

 

# Example 1:

# Input: root = [2,1,3]
# Output: [2,1,3]
# Example 2:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 10**4].
# 0 <= Node.val <= 10**4
# The input tree is guaranteed to be a binary search tree.


# Idea: use BFS. also save "None" if child is None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if root is None:
            return ''
        my_q=deque()
        my_q.append(root)
        result_list=[]
        while my_q:
            q_size=len(my_q)
            for i in range(q_size):
                a_node=my_q.popleft()
                if a_node is None:
                    result_list.append(str(-1))
                else:
                    result_list.append(str(a_node.val))
                    my_q.append(a_node.left)
                    my_q.append(a_node.right)
        

        return '|'.join(result_list)
        


        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """

        if data=='':
            return None
        result_list=data.split('|')

        root=TreeNode(int(result_list[0]))
        my_q=deque([root])

        for i in range(1, len(result_list), 2):
            #left, then right
            a_node=my_q.popleft()
            if result_list[i]!='-1':
                new_node=TreeNode(int(result_list[i]))
                my_q.append(new_node)
                a_node.left=new_node
            else:
                a_node.left=None

            if result_list[i+1]!='-1':
                new_node=TreeNode(int(result_list[i+1]))
                my_q.append(new_node)
                a_node.right=new_node
            else:
                a_node.right=None

        return root



        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

