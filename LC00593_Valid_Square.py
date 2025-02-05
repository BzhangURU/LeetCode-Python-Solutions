# LC00593_Valid_Square.py

# Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

# The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

# A valid square has four equal sides with positive length and four equal angles (90-degree angles).

 

# Example 1:

# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: true
# Example 2:

# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
# Output: false
# Example 3:

# Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
# Output: true
 

# Constraints:

# p1.length == p2.length == p3.length == p4.length == 2
# -10**4 <= xi, yi <= 10**4

# My idea: randomly use one point as anchor, the dis**2 ratio should be exactly a**2 : b**2 : c**2==1:1:2
# (a,b,c are vectors) then ac==bc, ab==0 


from typing import List
from functools import cmp_to_key

def cmp(x,y):
    return (x[0]*x[0]+x[1]*x[1])-(y[0]*y[0]+y[1]*y[1])

def get_sq_dis(x):
    return x[0]*x[0]+x[1]*x[1]

def inner_product(x,y):
    return x[0]*y[0]+x[1]*y[1]

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        vectors=[[p2[0]-p1[0],p2[1]-p1[1]],[p3[0]-p1[0],p3[1]-p1[1]],[p4[0]-p1[0],p4[1]-p1[1]]]

        vectors.sort(key=cmp_to_key(cmp))

        if get_sq_dis(vectors[0])==0:
            return False
        if get_sq_dis(vectors[0])!=get_sq_dis(vectors[1]):
            return False
        if 2*get_sq_dis(vectors[0])!=get_sq_dis(vectors[2]):
            return False
        if inner_product(vectors[0], vectors[1])!=0:
            return False
        if inner_product(vectors[0], vectors[2])!=inner_product(vectors[1], vectors[2]):
            return False
        return True
