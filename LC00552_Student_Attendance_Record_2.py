# LC00552_Student_Attendance_Record_2.py

# An attendance record for a student can be represented as a string where each character 
# signifies whether the student was absent, late, or present on that day. The record only 
# contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# Any student is eligible for an attendance award if they meet both of the following criteria:

# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Given an integer n, return the number of possible attendance records of length n that make a 
# student eligible for an attendance award. The answer may be very large, so return it modulo 10^9 + 7.

 

# Example 1:

# Input: n = 2
# Output: 8
# Explanation: There are 8 records with length 2 that are eligible for an award:
# "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
# Example 2:

# Input: n = 1
# Output: 3
# Example 3:

# Input: n = 10101
# Output: 183236316
 

# Constraints:

# 1 <= n <= 10^5

# Idea: dynamic programming, save 6 states of each step: 0A_end_has_0L, 0A_end_has_1L, 0A_end_has_2L, 1A_end_has_0L, 1A_end_has_1L, 1A_end_has_2L


class Solution:
    def checkRecord(self, n: int) -> int:
        dp_0A=[[0,0,0] for _ in range(n+1)]
        dp_1A=[[0,0,0] for _ in range(n+1)]

        # n=1
        dp_0A[1][0]=1#0A 0L, just 'P'
        dp_0A[1][1]=1#0A 1L, just 'L'
        dp_0A[1][2]=0#0A 2L, not exist

        dp_1A[1][0]=1#1A 0L, just 'A'
        dp_1A[1][1]=0#1A 1L, not exist
        dp_1A[1][2]=0#1A 2L, not exist

        modulo=10**9+7

        # for i in range(2,n+1):
        #     dp_0A[i][0]=dp_0A[i-1][0]+dp_0A[i-1][1]+dp_0A[i-1][2]# append 'P'
        #     dp_0A[i][1]=dp_0A[i-1][0]#previous has no 'L' in the end, append 'L'
        #     dp_0A[i][2]=dp_0A[i-1][1]

        #     dp_1A[i][0]=dp_1A[i-1][0]+dp_1A[i-1][1]+dp_1A[i-1][2]+dp_0A[i-1][0]+dp_0A[i-1][1]+dp_0A[i-1][2]# append 'P' or append 'A'
        #     dp_1A[i][1]=dp_1A[i-1][0]#previous has no 'L' in the end, append 'L'
        #     dp_1A[i][2]=dp_1A[i-1][1]

        for i in range(2,n+1):
            dp_0A[i][0]=(dp_0A[i-1][0]+dp_0A[i-1][1]+dp_0A[i-1][2])%modulo# append 'P'
            dp_0A[i][1]=dp_0A[i-1][0]#previous has no 'L' in the end, append 'L'
            dp_0A[i][2]=dp_0A[i-1][1]

            dp_1A[i][0]=(dp_1A[i-1][0]+dp_1A[i-1][1]+dp_1A[i-1][2]+dp_0A[i-1][0]+dp_0A[i-1][1]+dp_0A[i-1][2])%modulo# append 'P' or append 'A'
            dp_1A[i][1]=dp_1A[i-1][0]#previous has no 'L' in the end, append 'L'
            dp_1A[i][2]=dp_1A[i-1][1]

        return (dp_0A[n][0]+dp_0A[n][1]+dp_0A[n][2]+dp_1A[n][0]+dp_1A[n][1]+dp_1A[n][2])%modulo

my_solu=Solution()
result=my_solu.checkRecord(101)
print(result)
