
# LC00812_Largest_Triangle_Area.py

# Given an array of points on the X-Y plane points where points[i] = [xi, yi], 
# return the area of the largest triangle that can be formed by any three different points. 
# Answers within 10-5 of the actual answer will be accepted.

 

# Example 1:


# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2.00000
# Explanation: The five points are shown in the above figure. The red triangle is the largest.
# Example 2:

# Input: points = [[1,0],[0,0],[0,1]]
# Output: 0.50000
 

# Constraints:

# 3 <= points.length <= 50
# -50 <= xi, yi <= 50
# All the given points are unique.

#Idea: use cross product /2 to calculate area

class Solution:
    def area_of_three_points(self,point1, point2,point3):
        v1=[point2[0]-point1[0],point2[1]-point1[1]]
        v2=[point3[0]-point1[0],point3[1]-point1[1]]
        area=abs(v1[0]*v2[1]-v1[1]*v2[0])/2
        return area
        
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area=0.0
        for p1_ind in range(len(points)):
            for p2_ind in range(p1_ind+1,len(points)):
                for p3_ind in range(p2_ind+1,len(points)):
                    cur_area=self.area_of_three_points(points[p1_ind],points[p2_ind],points[p3_ind])
                    if cur_area>max_area:
                        max_area=cur_area
        return max_area







        
