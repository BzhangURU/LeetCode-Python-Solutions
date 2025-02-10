# LC00307_Range_Sum_Query_Mutable.py

# Given an integer array nums, handle multiple queries of the following types:

# Update the value of an element in nums.
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# void update(int index, int val) Updates the value of nums[index] to be val.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices 
# left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

# Example 1:

# Input
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# Output
# [null, 9, null, 8]

# Explanation
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1, 2, 5]
# numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
 

# Constraints:

# 1 <= nums.length <= 3 * 10**4
# -100 <= nums[i] <= 100
# 0 <= index < nums.length
# -100 <= val <= 100
# 0 <= left <= right < nums.length
# At most 3 * 10**4 calls will be made to update and sumRange.

#Idea: use binary tree, each leaf saves a num, each non-leaf node saves sum, 
# to update, we just need to update leaf's ancestors' sum.
# to sumRange, we run sum before left, then run sum before right.
# to get sum before an index, we start from root, if we go to a left child, we deduct the sum in right child.

from typing import List

class TreeNode:
    def __init__(self,val,left_list_last_index, left=None,right=None):
        self.val=val
        self.left_list_last_index=left_list_last_index
        self.left=left
        self.right=right

def build_tree(node,nums,left_ind,right_ind):#inclusive
    if left_ind==right_ind:
        node.val=nums[left_ind]
        node.left_list_last_index=-1
    else:
        half_ind=(left_ind+right_ind)//2
        node.val=0
        node.left_list_last_index=half_ind
        left_child=TreeNode(0,0)
        right_child=TreeNode(0,0)
        node.left=left_child
        node.right=right_child
        build_tree(left_child,nums,left_ind,half_ind)
        build_tree(right_child,nums,half_ind+1,right_ind)

def cal_sum(node):
    if node.left is None:
        return node.val
    else:
        node.val=cal_sum(node.left)+cal_sum(node.right)
        return node.val
    
class NumArray:

    def __init__(self, nums: List[int]):
        self.root=TreeNode(0,0)
        self.nums=nums
        build_tree(self.root,nums,0,len(nums)-1)
        #calculate non-leaf node's sum
        cal_sum(self.root)


    def update(self, index: int, val: int) -> None:
        assert index>=0 and index<len(self.nums)
        original_val=self.nums[index]
        sum_dif=val-original_val
        node=self.root
        while node.left is not None:
            node.val+=sum_dif
            if index<=node.left_list_last_index:
                node=node.left
            else:
                node=node.right
        node.val=val
        self.nums[index]=val

    def sumBefore(self, index):#include index
        sum_result=self.root.val
        node=self.root
        while node.left is not None:
            if index<=node.left_list_last_index:
                sum_result-=node.right.val
                node=node.left
            else:
                node=node.right
        return sum_result


    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.sumBefore(right)
        else:
            return self.sumBefore(right)-self.sumBefore(left-1)

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
