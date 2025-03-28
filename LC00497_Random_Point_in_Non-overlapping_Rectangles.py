# LC00497_Random_Point_in_Non-overlapping_Rectangles.py

# You are given an array of non-overlapping axis-aligned rectangles rects 
# where rects[i] = [ai, bi, xi, yi] indicates that (ai, bi) is the bottom-left 
# corner point of the ith rectangle and (xi, yi) is the top-right corner point 
# of the ith rectangle. Design an algorithm to pick a random integer point inside 
# the space covered by one of the given rectangles. A point on the perimeter of a 
# rectangle is included in the space covered by the rectangle.

# Any integer point inside the space covered by one of the given rectangles should 
# be equally likely to be returned.

# Note that an integer point is a point that has integer coordinates.

# Implement the Solution class:

# Solution(int[][] rects) Initializes the object with the given rectangles rects.
# int[] pick() Returns a random integer point [u, v] inside the space covered by 
# one of the given rectangles.
 

# Example 1:


# Input
# ["Solution", "pick", "pick", "pick", "pick", "pick"]
# [[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]
# Output
# [null, [1, -2], [1, -1], [-1, -2], [-2, -2], [0, 0]]

# Explanation
# Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]);
# solution.pick(); // return [1, -2]
# solution.pick(); // return [1, -1]
# solution.pick(); // return [-1, -2]
# solution.pick(); // return [-2, -2]
# solution.pick(); // return [0, 0]
 

# Constraints:

# 1 <= rects.length <= 100
# rects[i].length == 4
# -10**9 <= ai < xi <= 10**9
# -10**9 <= bi < yi <= 10**9
# xi - ai <= 2000
# yi - bi <= 2000
# All the rectangles do not overlap.
# At most 104 calls will be made to pick.

# Idea: calculate each rectangle's total integer points counts, sum them. 

import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.accumulated_sum=[]
        left, right, top, bottom = rects[0][0], rects[0][2], rects[0][3], rects[0][1]
        self.accumulated_sum.append((right-left+1)*(top-bottom+1))
        self.rects=rects
        for i in range(1, len(rects)):
            left, right, top, bottom = rects[i][0], rects[i][2], rects[i][3], rects[i][1]
            cur_sum=self.accumulated_sum[-1]
            self.accumulated_sum.append(cur_sum+(right-left+1)*(top-bottom+1))

        

    def pick(self) -> List[int]:
        total_sum=self.accumulated_sum[-1]
        rand_num=random.randrange(total_sum)
        #print('----------------------------')
        #first check which rectangle was chosen

        left_ind=0
        right_ind=len(self.accumulated_sum)-1
        while left_ind!=right_ind:
            middle_ind=(left_ind+right_ind)//2
            if rand_num>=self.accumulated_sum[middle_ind]:
                left_ind=middle_ind+1
            else:
                right_ind=middle_ind
        i=left_ind
        left, right, top, bottom = self.rects[i][0], self.rects[i][2], self.rects[i][3], self.rects[i][1]

        if i==0:
            point_ind=rand_num
        else:
            point_ind=rand_num-self.accumulated_sum[i-1]

        # print(self.accumulated_sum)
        # print(left_ind)
        # print(point_ind)
        # print(right-left)

        row=point_ind//(right-left+1)
        col=point_ind%(right-left+1)
        return [left+col, bottom+row]


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
