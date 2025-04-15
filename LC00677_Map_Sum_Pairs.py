# LC00677_Map_Sum_Pairs.py

# Design a map that allows you to do the following:

# Maps a string key to a given value.
# Returns the sum of the values that have a key with a prefix equal to a given string.
# Implement the MapSum class:

# MapSum() Initializes the MapSum object.
# void insert(String key, int val) Inserts the key-val pair into the map. 
# If the key already existed, the original key-value pair will be overridden to the new one.
# int sum(string prefix) Returns the sum of all the pairs' value whose key 
# starts with the prefix.
 

# Example 1:

# Input
# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
# Output
# [null, null, 3, null, 5]

# Explanation
# MapSum mapSum = new MapSum();
# mapSum.insert("apple", 3);  
# mapSum.sum("ap");           // return 3 (apple = 3)
# mapSum.insert("app", 2);    
# mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
 

# Constraints:

# 1 <= key.length, prefix.length <= 50
# key and prefix consist of only lowercase English letters.
# 1 <= val <= 1000
# At most 50 calls will be made to insert and sum.

# Idea: Trie-tree

class tree_node:
    def __init__(self, val=0):
        self.val=val
        self.children={}

class MapSum:

    def __init__(self):
        self.root_node=tree_node()

    def insert_nodes(self, key, cur_str_index, node, val):
        if key[cur_str_index] not in node.children:
            node.children[key[cur_str_index]]=tree_node()
        if cur_str_index==len(key)-1:
            node.children[key[cur_str_index]].val=val
        else:
            self.insert_nodes(key, cur_str_index+1, node.children[key[cur_str_index]], val)

    def insert(self, key: str, val: int) -> None:
        self.insert_nodes(key,0,self.root_node,val)

    def sum_all_subnodes(self, node, result_list):
        result_list[0]+=node.val
        if len(node.children)>0:
            for k,v in node.children.items():
                self.sum_all_subnodes(v,result_list)
            


    def sum(self, prefix: str) -> int:
        # first find the node through prefix
        node=self.root_node
        for i in range(len(prefix)):
            if prefix[i] in node.children:
                node=node.children[prefix[i]]
            else:
                return 0
            
        # then sum all the values
        result_list=[0]
        self.sum_all_subnodes(node, result_list)
        return result_list[0]

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


