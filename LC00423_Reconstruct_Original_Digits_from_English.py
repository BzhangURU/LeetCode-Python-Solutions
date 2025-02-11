# LC00423_Reconstruct_Original_Digits_from_English.py
# Given a string s containing an out-of-order English representation of digits 0-9, 
# return the digits in ascending order.

 

# Example 1:

# Input: s = "owoztneoer"
# Output: "012"
# Example 2:

# Input: s = "fviefuro"
# Output: "45"
 

# Constraints:

# 1 <= s.length <= 10**5
# s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
# s is guaranteed to be valid.

# ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]
#0: 1                   1           1                       1
#1: 1                   1   1            
#2:                     1                   1   1
#3: 2               1               1       1
#4:         1           1           1   1
#5: 1       1   1                                   1
#6:             1               1                       1
#7: 2                       1   1                   1
#8: 1   1       1   1                       1
#9: 1           1           2
# 
# first 0, 6, 2, 4, 8, because they have unique letter

# ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]
#1: 1                   1   1            
#3: 2               1               1       1
#5: 1       1   1                                   1
#7: 2                       1   1                   1
#9: 1           1           2
# 
#  then 5, 3, 1, 7

#then finally 9

class Solution:
    def originalDigits(self, s: str) -> str:
        letter_bin_dict={"e":0,"g":0,"f":0,"i":0,"h":0,"o":0,"n":0,"s":0,"r":0,"u":0,"t":0,"w":0,"v":0,"x":0,"z":0}

        for i in range(len(s)):
            letter_bin_dict[s[i]]+=1

        list_nums=[]

        z_0_count=letter_bin_dict['z']
        letter_bin_dict['z']-=z_0_count
        letter_bin_dict['e']-=z_0_count
        letter_bin_dict['r']-=z_0_count
        letter_bin_dict['o']-=z_0_count
        list_nums.extend([0]*z_0_count)

        w_2_count=letter_bin_dict['w']
        letter_bin_dict['t']-=w_2_count
        letter_bin_dict['w']-=w_2_count
        letter_bin_dict['o']-=w_2_count
        list_nums.extend([2]*w_2_count)

        u_4_count=letter_bin_dict['u']
        letter_bin_dict['f']-=u_4_count
        letter_bin_dict['o']-=u_4_count
        letter_bin_dict['u']-=u_4_count
        letter_bin_dict['r']-=u_4_count
        list_nums.extend([4]*u_4_count)

        x_6_count=letter_bin_dict['x']
        letter_bin_dict['s']-=x_6_count
        letter_bin_dict['i']-=x_6_count
        letter_bin_dict['x']-=x_6_count
        list_nums.extend([6]*x_6_count)

        g_8_count=letter_bin_dict['g']
        letter_bin_dict['e']-=g_8_count
        letter_bin_dict['i']-=g_8_count
        letter_bin_dict['g']-=g_8_count
        letter_bin_dict['h']-=g_8_count
        letter_bin_dict['t']-=g_8_count
        list_nums.extend([8]*g_8_count)

        o_1_count=letter_bin_dict['o']
        letter_bin_dict['o']-=o_1_count
        letter_bin_dict['n']-=o_1_count
        letter_bin_dict['e']-=o_1_count
        list_nums.extend([1]*o_1_count)

        h_3_count=letter_bin_dict['h']
        letter_bin_dict['t']-=h_3_count
        letter_bin_dict['h']-=h_3_count
        letter_bin_dict['r']-=h_3_count
        letter_bin_dict['e']-=h_3_count
        letter_bin_dict['e']-=h_3_count
        list_nums.extend([3]*h_3_count)

        f_5_count=letter_bin_dict['f']
        letter_bin_dict['f']-=f_5_count
        letter_bin_dict['i']-=f_5_count
        letter_bin_dict['v']-=f_5_count
        letter_bin_dict['e']-=f_5_count
        list_nums.extend([5]*f_5_count)

        s_7_count=letter_bin_dict['s']
        letter_bin_dict['s']-=s_7_count
        letter_bin_dict['e']-=s_7_count
        letter_bin_dict['v']-=s_7_count
        letter_bin_dict['e']-=s_7_count
        letter_bin_dict['n']-=s_7_count
        list_nums.extend([7]*s_7_count)

        i_9_count=letter_bin_dict['i']
        letter_bin_dict['n']-=i_9_count
        letter_bin_dict['i']-=i_9_count
        letter_bin_dict['n']-=i_9_count
        letter_bin_dict['e']-=i_9_count
        list_nums.extend([9]*i_9_count)

        list_nums.sort()
        list_str=[str(num) for num in list_nums]
        result=''.join(list_str)
        return result



        

