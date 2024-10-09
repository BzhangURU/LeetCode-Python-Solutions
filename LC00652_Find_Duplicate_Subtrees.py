#LC00652_Find_Duplicate_Subtrees

# Given the root of a binary tree, return all duplicate subtrees.

# For each kind of duplicate subtrees, you only need to return the root node of any one of them.

# Two trees are duplicate if they have the same structure with the same node values.

# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]

# Input: root = [2,1,1]
# Output: [[1]]

# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]

# Constraints:

# The number of the nodes in the tree will be in the range [1, 5000]
# -200 <= Node.val <= 200


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        
        #Convert tree to a string
        
        #str[start:end] forms a substring
        set_str_start_mapping_end={}
        set_str_start_mapping_node={}
        
        #save the start indeces of substrings that represent subtrees
        list_start_indices=[]
        
        #key is the string of subtree, value is count
        set_count_duplicate_subtree={}
        
        res_string=""
        res_string=self.traverse_tree(root,res_string, set_str_start_mapping_end, set_str_start_mapping_node, list_start_indices)
        
        output_list=[]
        
        for i in range(len(list_start_indices)):
            start_ind=list_start_indices[i]
            end_ind=set_str_start_mapping_end[start_ind]
            #if duplicate subtree exists
            if res_string[start_ind:end_ind] in set_str_start_mapping_end:
                current_count=set_str_start_mapping_end[res_string[start_ind:end_ind]]
                if current_count==1:
                    output_list.append(set_str_start_mapping_node[start_ind])
                set_str_start_mapping_end[res_string[start_ind:end_ind]]=current_count+1
            else:
                set_str_start_mapping_end[res_string[start_ind:end_ind]]=1
                
        return output_list
        
        
        
        
        
    #construct string from a tree
    def traverse_tree(self, node, res_string, set_str_start_mapping_end, set_str_start_mapping_node, list_start_indices):
        start_ind=len(res_string)
        list_start_indices.append(start_ind)
        set_str_start_mapping_node[start_ind]=node
        
        res_string=res_string+str(node.val)
        
        if node.left is not None:
            res_string=res_string+'('
            res_string=self.traverse_tree(node.left,res_string, set_str_start_mapping_end, set_str_start_mapping_node, list_start_indices)
            res_string=res_string+')'
            if node.right is not None:
                res_string=res_string+'('
                res_string=self.traverse_tree(node.right,res_string, set_str_start_mapping_end, set_str_start_mapping_node, list_start_indices)
                res_string=res_string+')'
        elif node.right is not None:
            res_string=res_string+'()('
            res_string=self.traverse_tree(node.right,res_string, set_str_start_mapping_end, set_str_start_mapping_node, list_start_indices)
            res_string=res_string+')'
            
        end_ind=len(res_string)
        set_str_start_mapping_end[start_ind]=end_ind
        
        return res_string
