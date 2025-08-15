# LC00729_My_Calendar1.py

# You are implementing a program to use as your calendar. We can add a new event 
# if adding the event will not cause a double booking.

# A double booking happens when two events have some non-empty intersection 
# (i.e., some moment is common to both events.).

# The event can be represented as a pair of integers startTime and endTime that 
# represents a booking on the half-open interval [startTime, endTime), the range 
# of real numbers x such that startTime <= x < endTime.

# Implement the MyCalendar class:

# MyCalendar() Initializes the calendar object.
# boolean book(int startTime, int endTime) Returns true if the event can be added 
# to the calendar successfully without causing a double booking. Otherwise, 
# return false and do not add the event to the calendar.
 

# Example 1:

# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]

# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time 15 
# is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the first 
# event takes every time less than 20, but not including 20.
 

# Constraints:

# 0 <= start < end <= 109
# At most 1000 calls will be made to book.

# Idea: maintain calendar in sorted order all the time. 

class MyCalendar:

    def __init__(self):
        self.calendar=[]
        

    def book(self, startTime: int, endTime: int) -> bool:
        if len(self.calendar)==0:
            self.calendar=[[startTime,endTime]]
            return True
        elif startTime<=self.calendar[0][0]:
            if endTime>self.calendar[0][0]:
                return False
            elif endTime==self.calendar[0][0]:
                self.calendar[0][0]=startTime
                return True
            else:
                self.calendar.insert(0,[startTime,endTime])
                return True
        elif self.calendar[-1][0]<=startTime:
            if startTime<self.calendar[-1][1]:
                return False
            elif startTime==self.calendar[-1][1]:
                self.calendar[-1][1]=endTime
                return True
            else:
                self.calendar.append([startTime,endTime])
                return True
        else:
            #find index i such that start time of index i <= startTime < start time of index (i+1)
            left=0
            right=len(self.calendar)-1
            while left+1<right:
                middle=(left+right)//2
                if self.calendar[middle][0]<=startTime:
                    left=middle
                else:
                    right=middle
            
            if startTime<self.calendar[left][1] or self.calendar[right][0]<endTime:
                return False
            elif self.calendar[left][1]<startTime and endTime<self.calendar[right][0]:
                self.calendar.insert(right,[startTime,endTime])
                return True
            elif self.calendar[left][1]==startTime and endTime<self.calendar[right][0]:
                self.calendar[left][1]=endTime
                return True
            elif self.calendar[left][1]<startTime and endTime==self.calendar[right][0]:
                self.calendar[right][0]=startTime
                return True
            elif self.calendar[left][1]==startTime and endTime==self.calendar[right][0]:
                interval=[self.calendar[left][0],self.calendar[right][1]]
                self.calendar[left:right+1]=[interval]
                return True
            else:
                raise ValueError('Wrong!')

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)


