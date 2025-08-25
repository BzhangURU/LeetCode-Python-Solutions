# LC00756_Pyramid_Transition_Matrix.py

# You are stacking blocks to form a pyramid. Each block has a color, which is 
# represented by a single letter. Each row of blocks contains one less block 
# than the row beneath it and is centered on top.

# To make the pyramid aesthetically pleasing, there are only specific triangular 
# patterns that are allowed. A triangular pattern consists of a single block stacked 
# on top of two blocks. The patterns are given as a list of three-letter strings allowed, 
# where the first two characters of a pattern represent the left and right bottom blocks 
# respectively, and the third character is the top block.

# For example, "ABC" represents a triangular pattern with a 'C' block stacked on top of 
# an 'A' (left) and 'B' (right) block. Note that this is different from "BAC" where 'B' 
# is on the left bottom and 'A' is on the right bottom.
# You start with a bottom row of blocks bottom, given as a single string, that you must 
# use as the base of the pyramid.

# Given bottom and allowed, return true if you can build the pyramid all the way to the 
# top such that every triangular pattern in the pyramid is in allowed, or false otherwise.

 

# Example 1:


# Input: bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
# Output: true
# Explanation: The allowed triangular patterns are shown on the right.
# Starting from the bottom (level 3), we can build "CE" on level 2 and then build "A" on level 1.
# There are three triangular patterns in the pyramid, which are "BCC", "CDE", and "CEA". All are allowed.
# Example 2:


# Input: bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]
# Output: false
# Explanation: The allowed triangular patterns are shown on the right.
# Starting from the bottom (level 4), there are multiple ways to build level 3, but trying all the 
# possibilites, you will get always stuck before building level 1.
 

# Constraints:

# 2 <= bottom.length <= 6
# 0 <= allowed.length <= 216
# allowed[i].length == 3
# The letters in all input strings are from the set {'A', 'B', 'C', 'D', 'E', 'F'}.
# All the values of allowed are unique.

# Idea: use a list to list all blocks from bottom to top, depth first search.

class Solution:
    def myPyramid(self,all_blocks,two_bottom_candidates,cur_ind_from_this_level,total_in_this_level):
        if total_in_this_level==1:
            if all_blocks[0-total_in_this_level-1]+all_blocks[0-total_in_this_level] in two_bottom_candidates:
                return True
            else:
                return False
            
        bottom2=all_blocks[0-total_in_this_level-1]+all_blocks[0-total_in_this_level]
        if bottom2 not in two_bottom_candidates:
            return False
        possible_letters=two_bottom_candidates[bottom2]
        
        for letter in possible_letters:#in set
            all_blocks.append(letter)
            if cur_ind_from_this_level<total_in_this_level-1:
                if cur_ind_from_this_level==0 or all_blocks[-2]+all_blocks[-1] in two_bottom_candidates:
                    if self.myPyramid(all_blocks,two_bottom_candidates,cur_ind_from_this_level+1,\
                                        total_in_this_level)==True:
                        return True
            else:
                if self.myPyramid(all_blocks,two_bottom_candidates,0,\
                                    total_in_this_level-1)==True:
                    return True
            all_blocks.pop()

        return False
        
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        two_bottom_candidates={}

        for str3 in allowed:
            if str3[0:2] in two_bottom_candidates:
                two_bottom_candidates[str3[0:2]].add(str3[2])
            else:
                two_bottom_candidates[str3[0:2]]=set([str3[2]])

        all_blocks=list(bottom)
        return self.myPyramid(all_blocks,two_bottom_candidates,0,len(bottom)-1)

            

bottom = "BCD"
allowed = ["BCC","CDE","CEA","FFF"]

my_solu=Solution()
my_solu.pyramidTransition(bottom,allowed)
        


        

