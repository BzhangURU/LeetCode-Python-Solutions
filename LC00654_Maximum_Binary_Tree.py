##LC00654_Maximum_Binary_Tree

# You are given an integer array nums with no duplicates. A maximum binary tree can be 
# built recursively from nums using the following algorithm:

# Create a root node whose value is the maximum value in nums.
# Recursively build the left subtree on the subarray prefix to the left of the maximum value.
# Recursively build the right subtree on the subarray suffix to the right of the maximum value.
# Return the maximum binary tree built from nums.

# Input: nums = [3,2,1,6,0,5]
# Output: [6,3,5,null,2,0,null,null,1]
# Explanation: The recursive calls are as follow:
# - The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
#     - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
#         - Empty array, so no child.
#         - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
#             - Empty array, so no child.
#             - Only one element, so child is a node with value 1.
#     - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
#         - Only one element, so child is a node with value 0.
#         - Empty array, so no child.
        
# Input: nums = [3,2,1]
# Output: [3,null,2,null,1]
 

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# All integers in nums are unique.
        


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def construct_tree(self,nums,left,right):
        if left+1==right:
            return TreeNode(nums[left])
        elif left==right:
            return None
        max_num=max(nums[left:right])
        for i in range(left,right):
            if max_num==nums[i]:
                break
        node=TreeNode(max_num,self.construct_tree(nums,left,i),self.construct_tree(nums,i+1,right))
        return node
        
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.construct_tree(nums, 0, len(nums))
