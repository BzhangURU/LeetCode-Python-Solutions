# LC00564_Find_the_Closest_Palindrome.py

# Given a string n representing an integer, return the closest integer (not including itself), 
# which is a palindrome. If there is a tie, return the smaller one.

# The closest is defined as the absolute difference minimized between two integers.

 

# Example 1:

# Input: n = "123"
# Output: "121"
# Example 2:

# Input: n = "1"
# Output: "0"
# Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
 

# Constraints:

# 1 <= n.length <= 18
# n consists of only digits.
# n does not have leading zeros.
# n is representing an integer in the range [1, 10^18 - 1].

# Idea: if n is already a palindrome, change the middle part to lower or higher
# If n is not a palindrome, change the tail part to lower or higher.
# After changing, add/minus the difference to original number to get another number.
# For example, 101-->111, then 101-(111-101)=91. Then search palindrome for 91-->99, finally get 99.

class Solution:
    def get_smaller_higher_palindrome(self, n):
        # 979--> return 969, 989, and 969 will be the answer
        # 909--> return -1, 919
        # 919--> return 909, 929
        # 999--> return 989, -1
        # 9999-> return 9889, -1

        # 9109-->return -1, 9119
        # 12932--> return 12921, -1
        # 123567-->return 123321, -1
        char_list=list(n)
        if n[::-1]!=n:#if not palindrom
            for i in range(int(len(n)//2)):
                char_list[len(n)-1-i]=char_list[i]
            new_palin_str=''.join(char_list)
            if int(new_palin_str)<int(n):
                return int(new_palin_str), -1
            else:
                return -1, int(new_palin_str)

        else:
            middle_digit_str=n[len(n)//2]
            if middle_digit_str=='9':
                char_list[len(n)//2]='8'
                if len(n)%2==0:
                    char_list[len(n)//2-1]='8'
                new_palin_str=''.join(char_list)
                return int(new_palin_str), -1
            elif middle_digit_str=='0':
                char_list[len(n)//2]='1'
                if len(n)%2==0:
                    char_list[len(n)//2-1]='1'
                new_palin_str=''.join(char_list)
                return -1, int(new_palin_str)
            else:
                char_list[len(n)//2]=chr(ord(middle_digit_str)-1)
                if len(n)%2==0:
                    char_list[len(n)//2-1]=chr(ord(middle_digit_str)-1)
                lower_palin_str=''.join(char_list)
                char_list[len(n)//2]=chr(ord(middle_digit_str)+1)
                if len(n)%2==0:
                    char_list[len(n)//2-1]=chr(ord(middle_digit_str)+1)
                higher_palin_str=''.join(char_list)
                return int(lower_palin_str), int(higher_palin_str)

    #single digit number will not call this function
    def add_one_to_first_half_digits(self, n:str) -> int:
        #99xx-->10000
        #99x->1000
        char_list=list(n)
        first_half_str=''.join(char_list[0:(len(n)+1)//2])
        first_half_str_plus_one=str(int(first_half_str)+1)
        appended_zeros=['0']*(len(n)-(len(n)+1)//2)
        appended_str=''.join(appended_zeros)
        result_str=first_half_str_plus_one+appended_str
        return int(result_str)

    #single digit number will not call this function
    def minus_one_to_first_half_digits(self, n:str) -> int:
        #10xx-->999
        #10x->99
        #1x-->9
        char_list=list(n)
        first_half_str=''.join(char_list[0:(len(n)+1)//2])
        first_half_str_minus_one=str(int(first_half_str)-1)#could be '0'
        appended_zeros=['9']*(len(n)-(len(n)+1)//2)
        appended_str=''.join(appended_zeros)
        result_str=first_half_str_minus_one+appended_str
        return int(result_str)

            
    def nearestPalindromic(self, n: str) -> str:
        lower_palin_int, higher_palin_int=self.get_smaller_higher_palindrome(n)

        #print(lower_palin_int, higher_palin_int)
        if lower_palin_int>=0 and higher_palin_int>=0:
            if len(n)==2 and lower_palin_int<10:#'11'
                return '9'
            return str(lower_palin_int)
        elif lower_palin_int>=0 and higher_palin_int==-1:
            dif_int=int(n)-lower_palin_int
            candidate=lower_palin_int
            #higher_bound_int=int(n)+dif_int
            higher_bound_int=self.add_one_to_first_half_digits(n)
            #if higher_bound_int's first half digits are dif with n, then we add 1 to the first half digits

            l_higher_bound_int, h_higher_bound_int=self.get_smaller_higher_palindrome(str(higher_bound_int))
            #print('lower_palin_int>=0 and higher_palin_int==-1')
            #print(l_higher_bound_int, h_higher_bound_int)
            if l_higher_bound_int>=0 and abs(l_higher_bound_int-int(n))<dif_int:
                candidate=l_higher_bound_int
                dif_int=abs(l_higher_bound_int-int(n))
            if h_higher_bound_int>=0 and abs(h_higher_bound_int-int(n))<dif_int:
                candidate=h_higher_bound_int
                dif_int=abs(h_higher_bound_int-int(n))
            return str(candidate)
        elif lower_palin_int==-1 and higher_palin_int>=0:
            dif_int=higher_palin_int-int(n)
            candidate=higher_palin_int
            #lower_bound_int=int(n)-dif_int
            lower_bound_int=self.minus_one_to_first_half_digits(n)
            l_lower_bound_int, h_lower_bound_int=self.get_smaller_higher_palindrome(str(lower_bound_int))
            #print('lower_palin_int==-1 and higher_palin_int>=0:')
            #print(l_lower_bound_int, h_lower_bound_int)

            if h_lower_bound_int>=0 and abs(h_lower_bound_int-int(n))<=dif_int:#here, is <=, not <. Because if it's a tie, we return smaller one
                candidate=h_lower_bound_int
                dif_int=abs(h_lower_bound_int-int(n))

                #in case n=='10', lower_bound_int=='9'
            if str(lower_bound_int)[::-1]==str(lower_bound_int) and abs(lower_bound_int-int(n))<=dif_int:
                candidate=lower_bound_int
                dif_int=abs(lower_bound_int-int(n))
            if l_lower_bound_int>=0 and abs(l_lower_bound_int-int(n))<=dif_int:# h_lower_bound_int first, then l_lower_bound_int. Because if it's a tie, we return smaller one
                candidate=l_lower_bound_int
                dif_int=abs(l_lower_bound_int-int(n))
            return str(candidate)
        else:
            raise ValueError
