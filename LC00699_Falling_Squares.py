# LC00699_Falling_Squares.py

# There are several squares being dropped onto the X-axis of a 2D plane.

# You are given a 2D integer array positions where positions[i] = [lefti, sideLengthi] 
# epresents the ith square with a side length of sideLengthi that is dropped with its 
# left edge aligned with X-coordinate lefti.

# Each square is dropped one at a time from a height above any landed squares. It then 
# falls downward (negative Y direction) until it either lands on the top side of another 
# square or on the X-axis. A square brushing the left/right side of another square does 
# not count as landing on it. Once it lands, it freezes in place and cannot be moved.

# After each square is dropped, you must record the height of the current tallest stack 
# of squares.

# Return an integer array ans where ans[i] represents the height described above after 
# dropping the ith square.

 

# Example 1:


# Input: positions = [[1,2],[2,3],[6,1]]
# Output: [2,5,5]
# Explanation:
# After the first drop, the tallest stack is square 1 with a height of 2.
# After the second drop, the tallest stack is squares 1 and 2 with a height of 5.
# After the third drop, the tallest stack is still squares 1 and 2 with a height of 5.
# Thus, we return an answer of [2, 5, 5].
# Example 2:

# Input: positions = [[100,100],[200,100]]
# Output: [100,100]
# Explanation:
# After the first drop, the tallest stack is square 1 with a height of 100.
# After the second drop, the tallest stack is either square 1 or square 2, both with heights of 100.
# Thus, we return an answer of [100, 100].
# Note that square 2 only brushes the right side of square 1, which does not count as landing on it.
 

# Constraints:

# 1 <= positions.length <= 1000
# 1 <= lefti <= 10**8
# 1 <= sideLengthi <= 10**6

from typing import List
# Idea: keep recording the heights in different slot, then update it when a new squre come. 

class Solution:
    def find_affected_indexes(self, height_list, left_pos, right_pos):
        # first find height_list_start_ind
        left_ind=0
        if right_pos<=height_list[left_ind][0]:
            return -1,-1#first -1 means there is no intersection, second -1 means new pos is at the left of index 0
        elif left_pos<height_list[left_ind][1]:
            #there is intersection with first element in height_list
            height_list_start_ind=0
            if len(height_list)==1:
                return 0,0
        elif len(height_list)==1:
            if height_list[left_ind][1]<=left_pos:
                return -1,0#-1 means there is no intersection, 0 means new pos is at the right of index 0
            else:
                return -1,-1
        else:
            left_ind=1
            right_ind=len(height_list)-1
            while left_ind!=right_ind:
                middle_ind=(left_ind+right_ind)//2
                if height_list[middle_ind][1]<=left_pos:
                    left_ind=middle_ind+1
                else:
                    right_ind=middle_ind
            if height_list[left_ind][1]<=left_pos:
                return -1,left_ind
            elif right_pos<=height_list[left_ind][0]:
                return -1,left_ind-1
            else:#there is intersection
                height_list_start_ind=left_ind

        # height_list[height_list_start_ind] definitely has intersection with [pos_left, pos_right] in here

        #then find height_list_last_ind
        right_ind=len(height_list)-1
        if height_list_start_ind==len(height_list)-1:
            return height_list_start_ind,height_list_start_ind
        while left_ind!=right_ind:
            middle_ind=(left_ind+right_ind+1)//2
            if right_pos<=height_list[middle_ind][0]:#height_list[middle_ind][1]<=left_pos:
                right_ind=middle_ind-1
            else:
                left_ind=middle_ind

        return height_list_start_ind,left_ind



    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        #height_list is like [ [left0, right0, height0], [left1, right1, height1] ], no overlapping
        height_list=[[positions[0][0], positions[0][0]+positions[0][1],positions[0][1] ]] 
        result_track_tallest_height=[positions[0][1]]
        #print(height_list)

        for i in range(1, len(positions)):
            
            left_pos=positions[i][0]
            right_pos=positions[i][0]+positions[i][1]
            #print(f'\ni={i}, left_pos= {left_pos}, right_pos={right_pos}, square height={right_pos-left_pos}')

            #find index range that affect falling of square positions[i]
            height_list_start_ind, height_list_last_ind=self.find_affected_indexes(height_list, left_pos, right_pos)

            #print(height_list_start_ind, height_list_last_ind)

            if height_list_start_ind==-1:#nothing affects falling of square positions[i]
                if height_list_last_ind>=0:
                    #this is last index before the new square

                    height_list.insert(height_list_last_ind+1, [left_pos,right_pos,positions[i][1]])

                    #check if merge is needed
                    if len(height_list)>height_list_last_ind+2 and height_list[height_list_last_ind+1][1]==height_list[height_list_last_ind+2][0] and \
                    height_list[height_list_last_ind+1][2]==height_list[height_list_last_ind+2][2]:
                        height_list[height_list_last_ind+1][1]=height_list[height_list_last_ind+2][1]
                        del height_list[height_list_last_ind+2]

                    if len(height_list)>height_list_last_ind+1 and height_list[height_list_last_ind][1]==height_list[height_list_last_ind+1][0] and \
                    height_list[height_list_last_ind][2]==height_list[height_list_last_ind+1][2]:
                        height_list[height_list_last_ind][1]=height_list[height_list_last_ind+1][1]
                        del height_list[height_list_last_ind+1]

                else:
                    #the new squre is at the most left
                    height_list[0:0]=[[left_pos,right_pos,positions[i][1]]]
                    if len(height_list)>1 and height_list[1][0]==height_list[0][1] and \
                    height_list[0][2]==height_list[1][2]:
                        height_list[0][1]=height_list[1][1]
                        del height_list[1]

                max_height=result_track_tallest_height[-1]
                if max_height<positions[i][1]:
                    max_height=positions[i][1]
                result_track_tallest_height.append(max_height)

            else:

                max_height_between_start_last=-1
                for j in range(height_list_start_ind,height_list_last_ind+1):
                    if height_list[j][2]>max_height_between_start_last:
                        max_height_between_start_last=height_list[j][2]
                cur_height=max_height_between_start_last+positions[i][1]

                new_partial_height_list=[]
                if height_list[height_list_start_ind][0]<left_pos:
                    new_partial_height_list.append([height_list[height_list_start_ind][0],left_pos,height_list[height_list_start_ind][2]])
                new_partial_height_list.append([left_pos,right_pos,cur_height])
                if height_list[height_list_last_ind][1]>right_pos:
                    new_partial_height_list.append([right_pos,height_list[height_list_last_ind][1],height_list[height_list_last_ind][2]])

                if cur_height>result_track_tallest_height[-1]:
                    result_track_tallest_height.append(cur_height)
                else:
                    height_append=result_track_tallest_height[-1]
                    result_track_tallest_height.append(height_append)


                #maybe we have a slot back to back and has same height, we merge them
                if height_list_start_ind>0 and height_list[height_list_start_ind-1][1]==new_partial_height_list[0][0] and \
                height_list[height_list_start_ind-1][2]==new_partial_height_list[0][2]:
                    new_partial_height_list[0][0]=height_list[height_list_start_ind-1][0]
                    height_list_start_ind-=1

                if height_list_last_ind<len(height_list)-1 and new_partial_height_list[-1][1]==height_list[height_list_last_ind+1][0] and \
                new_partial_height_list[-1][2]==height_list[height_list_last_ind+1][2]:
                    new_partial_height_list[-1][1]=height_list[height_list_last_ind+1][1]
                    height_list_last_ind+=1

                height_list[height_list_start_ind: height_list_last_ind+1]=new_partial_height_list

            
            #print(height_list)
            #print(result_track_tallest_height[-1])
        return result_track_tallest_height

my_solu=Solution()
#positions = [[13259169,614936],[633696,602282],[34120526,531664],[909832,846630],[5790720,608795],[50628732,941784],[13382424,834960],[3596245,629947],[11687192,602370],[20752810,532662],[3661596,662521],[389620,544310],[7276211,680822],[25400940,724224],[72010620,534619]]#[[3,2],[8,3],[1,4],[8,10],[9,3]]
positions=[[13727012,621923],[8825241,553444],[15742545,506615],[27135078,903683],[15576000,621395],[17457144,713626],[21511006,558759],[57594228,606831],[19544152,634166],[2572752,854974],[4378081,801587],[6313472,571239],[1943536,634879],[3160884,578465],[47475969,878549],[78136626,503244],[770028,608671],[3276104,770040],[4775760,914104],[27679035,897217],[6060460,983433],[23271300,846560],[8124828,618979],[16588800,537300],[5861170,714178],[18151460,745897],[285501,544603],[7180365,621533],[17099686,513721],[5941386,774984],[15315830,578925],[14834088,689784],[46832604,949729],[487563,628425],[40574499,583218],[30804683,727020],[36578332,835550],[75573760,519815],[3636542,782645],[32544134,729581],[5516196,643868],[34908984,837983],[897396,507296],[47590089,892660],[18905700,544608],[1803648,869660],[4551775,935583],[9488852,959198],[332748,777277],[210848,628488],[2553579,949329],[8167661,875007],[25207488,513791],[2590034,611681],[51356274,570768],[8577030,940730],[51410264,553037]]
print(my_solu.fallingSquares(positions))
