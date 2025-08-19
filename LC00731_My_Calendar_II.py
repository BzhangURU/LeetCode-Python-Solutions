# LC00731_My_Calendar_II.py

# You are implementing a program to use as your calendar. We can add a new event 
# if adding the event will not cause a triple booking.

# A triple booking happens when three events have some non-empty intersection 
# (i.e., some moment is common to all the three events.).

# The event can be represented as a pair of integers startTime and endTime that 
# represents a booking on the half-open interval [startTime, endTime), 
# the range of real numbers x such that startTime <= x < endTime.

# Implement the MyCalendarTwo class:

# MyCalendarTwo() Initializes the calendar object.
# boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar 
# successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
 

# Example 1:

# Input
# ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
# [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
# Output
# [null, true, true, true, false, true, true]

# Explanation
# MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
# myCalendarTwo.book(10, 20); // return True, The event can be booked. 
# myCalendarTwo.book(50, 60); // return True, The event can be booked. 
# myCalendarTwo.book(10, 40); // return True, The event can be double booked. 
# myCalendarTwo.book(5, 15);  // return False, The event cannot be booked, because 
# it would result in a triple booking.
# myCalendarTwo.book(5, 10); // return True, The event can be booked, as it does not 
# use time 10 which is already double booked.
# myCalendarTwo.book(25, 55); // return True, The event can be booked, as the time in 
# [25, 40) will be double booked with the third event, the time [40, 50) will be single booked, 
# and the time [50, 55) will be double booked with the second event.
 

# Constraints:

# 0 <= start < end <= 10**9
# At most 1000 calls will be made to book.

# Hint: Store two sorted lists of intervals: one list will be all times that are at least single booked, 
# and another list will be all times that are definitely double booked. If none of the double bookings 
# conflict, then the booking will succeed, and you should update your single and double bookings accordingly.


class MyCalendarTwo:

    def __init__(self):
        self.atLeastSingleCalendar=[]
        self.doubleCalendar=[]

    def book(self, startTime: int, endTime: int) -> bool:
        if len(self.doubleCalendar)==0:
            pass
        elif startTime<=self.doubleCalendar[0][0]:
            if endTime>self.doubleCalendar[0][0]:
                return False
        elif self.doubleCalendar[-1][0]<=startTime:
            if startTime<self.doubleCalendar[-1][1]:
                return False
        else:
            #find index i such that start time of index i <= startTime < start time of index (i+1)
            left=0
            right=len(self.doubleCalendar)-1
            while left+1<right:
                middle=(left+right)//2
                if self.doubleCalendar[middle][0]<=startTime:
                    left=middle
                else:
                    right=middle
            
            if startTime<self.doubleCalendar[left][1] or self.doubleCalendar[right][0]<endTime:
                return False
            
        #we will reach here if we can successfully book current event without triple booking
        if len(self.atLeastSingleCalendar)==0:
            self.atLeastSingleCalendar=[[startTime,endTime]]
            return True
        elif startTime<=self.atLeastSingleCalendar[0][0]:
            if endTime>self.atLeastSingleCalendar[0][0]:

                

                start_merging_ind=0
                while start_merging_ind<len(self.atLeastSingleCalendar) and self.atLeastSingleCalendar[start_merging_ind][0]<=endTime:
                    intersection_left=self.atLeastSingleCalendar[start_merging_ind][0]
                    intersection_right=min(self.atLeastSingleCalendar[start_merging_ind][1], endTime)
                    if intersection_left<intersection_right:
                        self.bookDoubleCalendar(intersection_left,intersection_right)
                    start_merging_ind+=1

                self.atLeastSingleCalendar[0:start_merging_ind]=[[startTime,max(endTime,self.atLeastSingleCalendar[start_merging_ind-1][1])]]
                return True


                #return False
            elif endTime==self.atLeastSingleCalendar[0][0]:
                self.atLeastSingleCalendar[0][0]=startTime
                return True
            else:
                self.atLeastSingleCalendar.insert(0,[startTime,endTime])
                return True
        elif self.atLeastSingleCalendar[-1][0]<=startTime:
            if startTime<self.atLeastSingleCalendar[-1][1]:
                #self.bookDoubleCalendar(self.atLeastSingleCalendar[-1][0],startTime)
                self.bookDoubleCalendar(startTime,min(endTime,self.atLeastSingleCalendar[-1][1]))
                if self.atLeastSingleCalendar[-1][1]<endTime:
                    self.atLeastSingleCalendar[-1][1]=endTime
                return True
                #return False
            elif startTime==self.atLeastSingleCalendar[-1][1]:
                self.atLeastSingleCalendar[-1][1]=endTime
                return True
            else:
                self.atLeastSingleCalendar.append([startTime,endTime])
                return True
        else:
            #find index i such that start time of index i <= startTime < start time of index (i+1)
            left=0
            right=len(self.atLeastSingleCalendar)-1
            while left+1<right:
                middle=(left+right)//2
                if self.atLeastSingleCalendar[middle][0]<=startTime:
                    left=middle
                else:
                    right=middle
            
            if startTime<self.atLeastSingleCalendar[left][1] or self.atLeastSingleCalendar[right][0]<endTime:
                #return False
                if startTime<self.atLeastSingleCalendar[left][1]:
                    merging_ind=left
                    start_merging_ind=left
                else:
                    merging_ind=right
                    if startTime==self.atLeastSingleCalendar[left][1]:
                        start_merging_ind=left
                    else:
                        start_merging_ind=right

                while merging_ind<len(self.atLeastSingleCalendar) and self.atLeastSingleCalendar[merging_ind][0]<=endTime:
                    intersection_left=max(self.atLeastSingleCalendar[merging_ind][0],startTime)
                    intersection_right=min(self.atLeastSingleCalendar[merging_ind][1], endTime)
                    if intersection_left<intersection_right:
                        self.bookDoubleCalendar(intersection_left,intersection_right)
                    merging_ind+=1

                self.atLeastSingleCalendar[start_merging_ind:merging_ind]=[[min(startTime,self.atLeastSingleCalendar[start_merging_ind][0]),
                                        max(endTime,self.atLeastSingleCalendar[merging_ind-1][1])]]
                return True



            elif self.atLeastSingleCalendar[left][1]<startTime and endTime<self.atLeastSingleCalendar[right][0]:
                self.atLeastSingleCalendar.insert(right,[startTime,endTime])
                return True
            elif self.atLeastSingleCalendar[left][1]==startTime and endTime<self.atLeastSingleCalendar[right][0]:
                self.atLeastSingleCalendar[left][1]=endTime
                return True
            elif self.atLeastSingleCalendar[left][1]<startTime and endTime==self.atLeastSingleCalendar[right][0]:
                self.atLeastSingleCalendar[right][0]=startTime
                return True
            elif self.atLeastSingleCalendar[left][1]==startTime and endTime==self.atLeastSingleCalendar[right][0]:
                interval=[self.atLeastSingleCalendar[left][0],self.atLeastSingleCalendar[right][1]]
                self.atLeastSingleCalendar[left:right+1]=[interval]
                return True
            else:
                raise ValueError('Wrong!')
            
        

        

    def bookDoubleCalendar(self, startTime: int, endTime: int) -> bool:
        if len(self.doubleCalendar)==0:
            self.doubleCalendar=[[startTime,endTime]]
            return True
        elif startTime<=self.doubleCalendar[0][0]:
            if endTime>self.doubleCalendar[0][0]:
                return False
            elif endTime==self.doubleCalendar[0][0]:
                self.doubleCalendar[0][0]=startTime
                return True
            else:
                self.doubleCalendar.insert(0,[startTime,endTime])
                return True
        elif self.doubleCalendar[-1][0]<=startTime:
            if startTime<self.doubleCalendar[-1][1]:
                return False
            elif startTime==self.doubleCalendar[-1][1]:
                self.doubleCalendar[-1][1]=endTime
                return True
            else:
                self.doubleCalendar.append([startTime,endTime])
                return True
        else:
            #find index i such that start time of index i <= startTime < start time of index (i+1)
            left=0
            right=len(self.doubleCalendar)-1
            while left+1<right:
                middle=(left+right)//2
                if self.doubleCalendar[middle][0]<=startTime:
                    left=middle
                else:
                    right=middle
            
            if startTime<self.doubleCalendar[left][1] or self.doubleCalendar[right][0]<endTime:
                return False
            elif self.doubleCalendar[left][1]<startTime and endTime<self.doubleCalendar[right][0]:
                self.doubleCalendar.insert(right,[startTime,endTime])
                return True
            elif self.doubleCalendar[left][1]==startTime and endTime<self.doubleCalendar[right][0]:
                self.doubleCalendar[left][1]=endTime
                return True
            elif self.doubleCalendar[left][1]<startTime and endTime==self.doubleCalendar[right][0]:
                self.doubleCalendar[right][0]=startTime
                return True
            elif self.doubleCalendar[left][1]==startTime and endTime==self.doubleCalendar[right][0]:
                interval=[self.doubleCalendar[left][0],self.doubleCalendar[right][1]]
                self.doubleCalendar[left:right+1]=[interval]
                return True
            else:
                raise ValueError('Wrong!')
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
