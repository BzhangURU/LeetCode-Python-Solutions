# LC00715_Range_Module.py

# A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges 
# represented as half-open intervals and query about them.

# A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

# Implement the RangeModule class:

# RangeModule() Initializes the object of the data structure.
# void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. 
# Adding an interval that partially overlaps with currently tracked numbers 
# should add any numbers in the interval [left, right) that are not already tracked.
# boolean queryRange(int left, int right) Returns true if every real number 
# in the interval [left, right) is currently being tracked, and false otherwise.
# void removeRange(int left, int right) Stops tracking every real number currently 
# being tracked in the half-open interval [left, right).
 

# Example 1:

# Input
# ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
# [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
# Output
# [null, null, null, true, false, true]

# Explanation
# RangeModule rangeModule = new RangeModule();
# rangeModule.addRange(10, 20);
# rangeModule.removeRange(14, 16);
# rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
# rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
# rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)
 

# Constraints:

# 1 <= left < right <= 10**9
# At most 10**4 calls will be made to addRange, queryRange, and removeRange.


# Hint 1
# Maintain a sorted set of disjoint intervals. addRange and removeRange can be performed with time complexity linear to the size of this set; 
# queryRange can be performed with time complexity logarithmic to the size of this set.

# Idea: do the addRange and removeRange in linear time. 
# In addRange, the key is to update: firstAffectedIntervalInd, lastAffectedIntervalInd, newIntervalLeft, newIntervalRight
#               when it is finalized, we remove affected intervals, and replace them with [newIntervalLeft, newIntervalRight]

class RangeModule:

    def __init__(self):
        self.myList=[]
        
    def addRange(self, left: int, right: int) -> None:
        if len(self.myList)==0:
            self.myList.append([left,right])
        else:
            #get influenced intervals
            firstAffectedIntervalInd=-1#to remove
            lastAffectedIntervalInd=-1#to remove

            newIntervalLeft=0#to insert
            newIntervalRight=0
            finished=False


            ind=0
            while ind<len(self.myList):
                if firstAffectedIntervalInd==-1:#merging not started yet
                    if right<self.myList[ind][0]:
                        self.myList.insert(ind,[left,right])
                        ind+=1
                        finished=True
                        break
                    elif self.myList[ind][1]<left:
                        pass
                    else:
                        #start merging intervals
                        firstAffectedIntervalInd=ind
                        lastAffectedIntervalInd=ind
                        newIntervalLeft=min(left,self.myList[ind][0])
                        newIntervalRight=max(right,self.myList[ind][1])
                else:#merging already started yet
                    if right<self.myList[ind][0]:
                        self.myList[firstAffectedIntervalInd:lastAffectedIntervalInd+1]=[[newIntervalLeft,newIntervalRight]]
                        ind=firstAffectedIntervalInd
                        finished=True
                        break
                    else:
                        #merge intervals
                        lastAffectedIntervalInd=ind
                        newIntervalRight=max(newIntervalRight,self.myList[ind][1])
                ind+=1
            if finished==False:
                if firstAffectedIntervalInd==-1:
                    self.myList.append([left,right])
                else:
                    self.myList[firstAffectedIntervalInd:lastAffectedIntervalInd+1]=[[newIntervalLeft,newIntervalRight]]

    def queryRange(self, left: int, right: int) -> bool:
        if len(self.myList)==0:
            return False
        #if true, only one interval has overlapping with [left, right], AND self.myList[ind][0]<=left and right<=self.myList[ind][1]
        ind_l=0
        ind_r=len(self.myList)-1
        
        if left<=self.myList[ind_l][1]:
            if self.myList[ind_l][0]<=left and right<=self.myList[ind_l][1]:
                return True
            else:
                return False
        if self.myList[ind_r][0]<=right:
            if self.myList[ind_r][0]<=left and right<=self.myList[ind_r][1]:
                return True
            else:
                return False

        #only use "left" to search the only possible interval
        while ind_l<ind_r:
            ind_m=(ind_l+ind_r)//2
            if self.myList[ind_m][0]<=left and left<self.myList[ind_m][1]:
                ind_l=ind_m
                ind_r=ind_m
                break
            if left<self.myList[ind_m][0]:
                ind_r=ind_m-1
            elif self.myList[ind_m][1]<=left:
                ind_l=ind_m+1

        if ind_l>ind_r:
            return False
        
        #check that only possible interval
        if self.myList[ind_l][0]<=left and right<=self.myList[ind_l][1]:
            return True
        else:
            return False




    def removeRange(self, left: int, right: int) -> None:
        #in removeRange, the intervals will never merge, we can check intervals one by one
        if len(self.myList)>0:
            ind=0
            while ind<len(self.myList):
                if self.myList[ind][1]<left:
                    pass
                elif right<self.myList[ind][0]:
                    break
                elif left<=self.myList[ind][0] and self.myList[ind][1]<=right:
                    #totally remove
                    del self.myList[ind]
                    ind-=1
                elif self.myList[ind][0]<left and right<self.myList[ind][1]:
                    #break into two intervals
                    new_insert=[[self.myList[ind][0],left],[right,self.myList[ind][1]]]
                    self.myList[ind:ind+1]=new_insert
                    break
                elif self.myList[ind][0]<left:
                    self.myList[ind][1]=left
                elif right<self.myList[ind][1]:
                    self.myList[ind][0]=right
                else:
                    raise ValueError('Unexpected case.')
                ind+=1


        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

my_solu=RangeModule()
my_solu.addRange(6,8)
print("my_solu.addRange(6,8)")
print(my_solu.myList)

print("my_solu.removeRange(7,8)")
my_solu.removeRange(7,8)
print(my_solu.myList)

print("my_solu.removeRange(8,9))")
my_solu.removeRange(8,9)
print(my_solu.myList)

my_solu.addRange(8,9)
print("my_solu.addRange(8,9)")
print(my_solu.myList)

print("my_solu.removeRange(1,3))")
my_solu.removeRange(1,3)
print(my_solu.myList)

my_solu.addRange(1,8)
print("my_solu.addRange(1,8)")
print(my_solu.myList)

print("my_solu.queryRange(2,4)")
print(my_solu.queryRange(2,4))
print(my_solu.myList)

print("my_solu.queryRange(2,9)")
print(my_solu.queryRange(2,9))
print(my_solu.myList)






# my_solu=RangeModule()
# my_solu.addRange(5,6)
# print("my_solu.addRange(5,6)")
# print(my_solu.myList)

# my_solu.addRange(2,8)
# print("my_solu.addRange(2,8)")
# print(my_solu.myList)


# print("my_solu.queryRange(1,4)")
# print(my_solu.queryRange(1,4))
# print(my_solu.myList)

# print("my_solu.removeRange(2,4)")
# my_solu.removeRange(2,4)
# print(my_solu.myList)

# print("my_solu.queryRange(4,5)")
# print(my_solu.queryRange(4,5))
# print(my_solu.myList)


