# LC00457_Circular_Array_Loop.py

# You are playing a game involving a circular array of non-zero integers nums. Each nums[i] 
# denotes the number of indices forward/backward you must move if you are located at index i:

# If nums[i] is positive, move nums[i] steps forward, and
# If nums[i] is negative, move nums[i] steps backward.
# Since the array is circular, you may assume that moving forward from the last element puts 
# you on the first element, and moving backwards from the first element puts you on the last element.

# A cycle in the array consists of a sequence of indices seq of length k where:

# Following the movement rules above results in the repeating index sequence 
# seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
# Every nums[seq[j]] is either all positive or all negative.
# k > 1
# Return true if there is a cycle in nums, or false otherwise.

 

# Example 1:


# Input: nums = [2,-1,1,2,2]
# Output: true
# Explanation: The graph shows how the indices are connected. White nodes are jumping forward, 
# while red is jumping backward.
# We can see the cycle 0 --> 2 --> 3 --> 0 --> ..., and all of its nodes are white 
# (jumping in the same direction).
# Example 2:


# Input: nums = [-1,-2,-3,-4,-5,6]
# Output: false
# Explanation: The graph shows how the indices are connected. White nodes are jumping forward, 
# while red is jumping backward.
# The only cycle is of size 1, so we return false.
# Example 3:


# Input: nums = [1,-1,5,1,4]
# Output: true
# Explanation: The graph shows how the indices are connected. White nodes are jumping forward, 
# while red is jumping backward.
# We can see the cycle 0 --> 1 --> 0 --> ..., and while it is of size > 1, it has a node 
# jumping forward and a node jumping backward, so it is not a cycle.
# We can see the cycle 3 --> 4 --> 3 --> ..., and all of its nodes are white (jumping in the 
#                                                                             same direction).
 

# Constraints:

# 1 <= nums.length <= 5000
# -1000 <= nums[i] <= 1000
# nums[i] != 0


# Idea: O(n) in time and space complexity. use dict_visiting_nodes to save node:step pair for the path we are currently visiting, when we have a circle,
# we check if it is either all positive or all negative in the circle. If yes, return True, otherwise stop current search. 
# Then we put all the visited nodes in current path into set_already_visited_nodes.


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        set_already_visited_nodes=set()
        dict_visiting_nodes={}

        for i in range(len(nums)):
            #if i not in set_already_visited_nodes and i not in dict_visiting_nodes:
            if i not in set_already_visited_nodes:
                cur_num=i
                dict_visiting_nodes[cur_num]=0
                if nums[cur_num]>0:
                    cur_move_is_positive=True
                    start_step_of_cur_move=0#start from which step is has always been positive
                else:
                    cur_move_is_positive=False
                    start_step_of_cur_move=0
                cur_step=0
                next_num=(cur_num+nums[cur_num]+len(nums))%len(nums)
                while next_num not in set_already_visited_nodes and \
                                next_num !=cur_num:
                    cur_step+=1
                    if next_num in dict_visiting_nodes:
                        if nums[next_num]>0 and cur_move_is_positive and start_step_of_cur_move<=dict_visiting_nodes[next_num]:
                            return True
                        elif nums[next_num]<0 and not cur_move_is_positive and start_step_of_cur_move<=dict_visiting_nodes[next_num]:
                            return True
                        else:
                            break
                    else:
                        dict_visiting_nodes[next_num]=cur_step
                        if nums[cur_num]*nums[next_num]<0:
                            cur_move_is_positive=(nums[next_num]>0)
                            start_step_of_cur_move=cur_step
                        cur_num=next_num
                        next_num=(cur_num+nums[cur_num]+len(nums))%len(nums)

                # finished a path, put all nodes in dict_visiting_nodes to set

                for k,v in dict_visiting_nodes.items():
                    set_already_visited_nodes.add(k)
        return False



                


