# LC00587_Erect_the_Fence.py

# You are given an array trees where trees[i] = [xi, yi] represents the location of 
# a tree in the garden.

# Fence the entire garden using the minimum length of rope, as it is expensive. 
# The garden is well-fenced only if all the trees are enclosed.

# Return the coordinates of trees that are exactly located on the fence perimeter. 
# You may return the answer in any order.

 

# Example 1:


# Input: trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
# Explanation: All the trees will be on the perimeter of the fence except 
# the tree at [2, 2], which will be inside the fence.
# Example 2:


# Input: trees = [[1,2],[2,2],[4,2]]
# Output: [[4,2],[2,2],[1,2]]
# Explanation: The fence forms a line that passes through all the trees.
 

# Constraints:

# 1 <= trees.length <= 3000
# trees[i].length == 2
# 0 <= xi, yi <= 100
# All the given positions are unique.

# Idea: start from most bottom point, then set direction to (1,0), calculate all 
# inner product from (cur_point-->next_point) to (1,0), normalize it. (actually we are 
# calculating cosine). get the point the has largest cosine value. (if there is a tie,
# get the closest point.). 

from typing import List
def squared_normalized_inner_product_with_sign_kept(v1, v2):
    # sign(v1 dot v2)* ( (v1 dot v2)/(|v1| |v2|) ) * ( (v1 dot v2)/(|v1| |v2|) )
    part0=v1[0]*v2[0]+v1[1]*v2[1]
    part1=float(part0*part0)
    part2=float((v1[0]*v1[0]+v1[1]*v1[1])*(v2[0]*v2[0]+v2[1]*v2[1]))
    result=part1/part2
    if part0<0:
        result*=-1
    return result
class Solution:
    def get_most_bottom_tree_index(self, trees):
        tree=trees[0]
        result=0
        for i in range(1, len(trees)):
            if trees[i][1]<tree[1]:
                tree=trees[i]
                result=i

        return result


    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees)<2:
            return trees
        start_tree_index=self.get_most_bottom_tree_index(trees)
        cur_tree_index=start_tree_index
        previous_dir=(1,0)
        count_step=0
        result=[trees[start_tree_index]]
        set_avoid_duplicated_tree=set()
        set_avoid_duplicated_tree.add(start_tree_index)

        #while count_step==0 or cur_tree_index!=start_tree_index:
        while True:
            #find next tree
            best_normalized_inner_product=-2.0
            best_next_tree_index=-1
            best_next_tree_distance=0
            #best_dir=[0,0]
            for i in range(len(trees)):
                if i==cur_tree_index:
                    pass
                else:
                    new_dir=(trees[i][0]-trees[cur_tree_index][0],trees[i][1]-trees[cur_tree_index][1])
                    normalized_inner_product=squared_normalized_inner_product_with_sign_kept(previous_dir, new_dir)
                    new_distance=new_dir[0]*new_dir[0]+new_dir[1]*new_dir[1]
                    if normalized_inner_product>best_normalized_inner_product or \
                        (normalized_inner_product==best_normalized_inner_product and new_distance<best_next_tree_distance):
                        best_normalized_inner_product=normalized_inner_product
                        best_next_tree_index=i
                        best_next_tree_distance=new_distance
                        best_dir=new_dir

            if best_next_tree_index==start_tree_index:
                break
            if best_next_tree_index not in set_avoid_duplicated_tree:
                set_avoid_duplicated_tree.add(best_next_tree_index)
                result.append(trees[best_next_tree_index])
            cur_tree_index=best_next_tree_index
            previous_dir=best_dir
            count_step+=1
            if count_step>2*len(trees):
                raise ValueError(f'Exceed limit: count_step: {count_step}, len(trees): {len(trees)}')

        return result
