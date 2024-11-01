# LC03001_Minimum_Moves_to_Capture_The_Queen.py
# There is a 1-indexed 8 x 8 chessboard containing 3 pieces.

# You are given 6 integers a, b, c, d, e, and f where:

# (a, b) denotes the position of the white rook.
# (c, d) denotes the position of the white bishop.
# (e, f) denotes the position of the black queen.
# Given that you can only move the white pieces, return the minimum number of moves required to capture the black queen.

# Note that:

# Rooks can move any number of squares either vertically or horizontally, but cannot jump over other pieces.
# Bishops can move any number of squares diagonally, but cannot jump over other pieces.
# A rook or a bishop can capture the queen if it is located in a square that they can move to.
# The queen does not move.
 

# Example 1:


# Input: a = 1, b = 1, c = 8, d = 8, e = 2, f = 3
# Output: 2
# Explanation: We can capture the black queen in two moves by moving the white rook to (1, 3) then to (2, 3).
# It is impossible to capture the black queen in less than two moves since it is not being attacked by any of the pieces at the beginning.
# Example 2:


# Input: a = 5, b = 3, c = 3, d = 4, e = 5, f = 2
# Output: 1
# Explanation: We can capture the black queen in a single move by doing one of the following: 
# - Move the white rook to (5, 2).
# - Move the white bishop to (5, 2).
 

# Constraints:

# 1 <= a, b, c, d, e, f <= 8
# No two pieces are on the same square.

#My idea: the maximum steps is 2. The rook can always carch queen in 2 steps. 
# The most challenging part is bishop is in the way. 
# If queen and rook are not in same straight line, bishop will not be in the way. 
# If queen and rook are in the same straight line, and bishop is in the way, bishop can first move away, then rook will catch the queen. 



def abs_dis(g,h):
    if g>h:
        return g-h
    else:
        return h-g

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        #if rook can catch queen in one step
        if a==e:
            #make sure bishop is not in the way
            if c!=a:
                return 1
            elif (d>b and d>f) or (d<b and d<f):
                return 1
        elif b==f:
            if d!=b:
                return 1
            elif (c>a and c>e) or (c<a and c<e):
                return 1

        #if bishop can catch queen in one step
        if abs_dis(c,e)==abs_dis(d,f):
            #make sure rook is not in the way
            if abs_dis(a,e)!=abs_dis(b,f):
                return 1
            elif a<min(c,e) or a>max(c,e) or b<min(d,f) or b>max(d,f):
                return 1

        return 2

my_solu=Solution()
#my_solu.minMovesToCaptureTheQueen(4,3,3,4,2,5)#1
my_solu.minMovesToCaptureTheQueen(4,3,3,1,6,4)#1
