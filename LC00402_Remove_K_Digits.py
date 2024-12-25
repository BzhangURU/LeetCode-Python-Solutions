# LC00402_Remove_K_Digits.py

# Given string num representing a non-negative integer num, and an integer k, 
# return the smallest possible integer after removing k digits from num.

 

# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:

# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

# Constraints:

# 1 <= k <= num.length <= 10**5
# num consists of only digits.
# num does not have any leading zeros except for the zero itself.

# Idea: The first digit is really important, if we are able to change the first digit, 
# then we should try our best to lower the first digit. 
# So, if the following k digits's min is lower than first digit, then do it.
# For example: 3462564834867, k=5, then remove 346, then the problem becomes 2564834867, k=2
# If the following k digits's min digit is not smaller than first digit, then
# we don't change the first digit, leave the first digit alone, and visit the next digit and check again.
# To speed up, we put the following k digits's condition into a count bin (bin size is 10: 0-9), and track the min.
# If we leave the first digit alone, we delete one in count bin, and update min if necessary. 

class Solution:
    def my_removeKdigits(self, int_list, digits_deleted_bool_list,cur_ind,following_k_bin,bin_min,k):
        if k==0:
            return
        #print(int_list,cur_ind,k)
        assert len(int_list)-cur_ind>=k
        if len(int_list)-cur_ind==k:
            #delete all including cur_ind
            for i in range(cur_ind,len(int_list)):
                digits_deleted_bool_list[i]=True
        else:
            if bin_min[0]<int_list[cur_ind]:
                find_min_ind=cur_ind+1
                while int_list[find_min_ind]>bin_min[0] and find_min_ind-cur_ind<=k:
                    find_min_ind+=1
                assert find_min_ind-cur_ind<=k
                for i in range(cur_ind,find_min_ind):
                    digits_deleted_bool_list[i]=True
                    if i>cur_ind:
                        following_k_bin[int_list[i]]-=1
                following_k_bin[int_list[find_min_ind]]-=1
                for i in range(10):
                    if following_k_bin[i]>0:
                        bin_min[0]=i
                        break
                self.my_removeKdigits(int_list, digits_deleted_bool_list,find_min_ind,following_k_bin,bin_min,k-(find_min_ind-cur_ind))
            else:
                #we don't remove cur digit
                following_k_bin[int_list[cur_ind+1]]-=1
                if cur_ind+k+1<len(int_list):
                    following_k_bin[int_list[cur_ind+k+1]]+=1
                    if int_list[cur_ind+k+1]<=bin_min[0]:
                        bin_min[0]=int_list[cur_ind+k+1]
                    elif following_k_bin[bin_min[0]]==0:
                        for i in range(bin_min[0],10):
                            if following_k_bin[i]>0:
                                bin_min[0]=i
                                break
                else:
                    #we will delte all the following digits, no need to update bin_min
                    pass
                self.my_removeKdigits(int_list, digits_deleted_bool_list,cur_ind+1,following_k_bin,bin_min,k)


    def removeKdigits(self, num: str, k: int) -> str:
        char_list=list(num)
        if len(char_list)<=k:
            return '0'
        int_list=[int(char_list[i]) for i in range(len(char_list))]
        digits_deleted_bool_list=[False]*len(int_list)
        cur_ind=0

        following_k_bin=[0]*10
        bin_min=[10]
        for i in range(1,k+1):
            digit=int_list[i]
            following_k_bin[digit]+=1
            if bin_min[0]>digit:
                bin_min[0]=digit
        self.my_removeKdigits(int_list, digits_deleted_bool_list,cur_ind,following_k_bin,bin_min,k)
        result_char_list=[]
        is_first_digit=True
        for i in range(len(int_list)):
            if digits_deleted_bool_list[i]== False:
                if is_first_digit and int_list[i]==0:
                    continue
                result_char_list.append(str(int_list[i]))
                is_first_digit=False
        #print(int_list)
        #print(digits_deleted_bool_list)
        #print(result_char_list)
        result=''.join(result_char_list)
        if len(result)==0:
            result='0'
        return result
    
my_solu=Solution()
# num='112'
# k=1
num="9999999999991"
k=8
my_solu.removeKdigits(num,k)




        


