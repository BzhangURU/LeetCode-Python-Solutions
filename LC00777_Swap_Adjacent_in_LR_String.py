# LC00777_Swap_Adjacent_in_LR_String.py

# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", 
# a move consists of either replacing one occurrence of "XL" with "LX", or replacing 
# one occurrence of "RX" with "XR". Given the starting string start and the ending string result, 
# return True if and only if there exists a sequence of moves to transform start to result.



# Example 1:

# Input: start = "RXXLRXRXL", result = "XRLXXRRLX"
# Output: true
# Explanation: We can transform start to result following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# Example 2:

# Input: start = "X", result = "L"
# Output: false
 

# Constraints:

# 1 <= start.length <= 10**4
# start.length == result.length
# Both start and result will only consist of characters in 'L', 'R', and 'X'.

# Idea: XLR -> LXR, X can't pass through both L and R, X can only pass through either only L or R.
# RXXL can transform to RLXX, XXRL, XRLX

# Movement direction of X:
#   <-- --> --> <-- <--
# ...R...L...L...R...R...

# keep track of number of X that moved across each letter(L or R).

class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        onlyLR=start.replace('X','')
        result_onlyLR=result.replace('X','')
        if onlyLR!=result_onlyLR:
            return False
        
        if onlyLR=='':
            return True
        
        #count number of continous 'X' between intervals 
        # LXRXXRXXX will generate 0,1,2,3

        count_X_intervals_start=[]
        count=0
        for i in range(len(start)):
            if start[i]!='X':
                count_X_intervals_start.append(count)
                count=0
            else:
                count+=1
        count_X_intervals_start.append(count)

        count_X_intervals_result=[]
        count=0
        for i in range(len(result)):
            if result[i]!='X':
                count_X_intervals_result.append(count)
                count=0
            else:
                count+=1
        count_X_intervals_result.append(count)

        # count X that moved across letter(L or R)
        count_X_moved_right=0

        for i in range(len(onlyLR)):
            if onlyLR[i]=='L':
                if count_X_intervals_start[i]+count_X_moved_right<count_X_intervals_result[i]:
                    return False
                else:
                    #update count_X_moved_right
                    count_X_moved_right=count_X_intervals_start[i]+count_X_moved_right-count_X_intervals_result[i]
            else:
                if count_X_intervals_start[i]+count_X_moved_right>count_X_intervals_result[i]:
                    return False
                else:
                    count_X_moved_right=count_X_intervals_start[i]+count_X_moved_right-count_X_intervals_result[i]

        if count_X_intervals_start[len(onlyLR)]+count_X_moved_right!=count_X_intervals_result[len(onlyLR)]:
            return False
        else:
            return True


start = "RXXLRXRXL"
result = "XRLXXRRLX"
#0,2,0,1,1,0
#1,0,2,0,0,1
my_solu=Solution()
print(my_solu.canTransform(start,result))
