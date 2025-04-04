# LC00468_Validate_IP_Address.py

# Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or 
# "Neither" if IP is not a correct IP of any type.

# A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. 
# For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", 
# and "192.168@1.1" are invalid IPv4 addresses.

# A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

# 1 <= xi.length <= 4
# xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and 
# upper-case English letters ('A' to 'F').
# Leading zeros are allowed in xi.
# For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are 
# valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

 

# Example 1:

# Input: queryIP = "172.16.254.1"
# Output: "IPv4"
# Explanation: This is a valid IPv4 address, return "IPv4".
# Example 2:

# Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
# Output: "IPv6"
# Explanation: This is a valid IPv6 address, return "IPv6".
# Example 3:

# Input: queryIP = "256.256.256.256"
# Output: "Neither"
# Explanation: This is neither a IPv4 address nor a IPv6 address.
 

# Constraints:

# queryIP consists only of English letters, digits and the characters '.' and ':'.

def is_valid_v4_part(a_part):
    if len(a_part)==0 or len(a_part)>3:
        return False
    for i in range(len(a_part)):
        if ord(a_part[i])>ord('9') or ord(a_part[i])<ord('0'):
            return False
    if len(a_part)>1 and a_part[0]=='0':
        return False
    int_num=int(a_part)
    if int_num>255:
        return False
    return True

def is_valid_v6_part(a_part):
    if len(a_part)==0 or len(a_part)>4:
        return False
    for i in range(len(a_part)):
        if (ord(a_part[i])<=ord('9') and ord(a_part[i])>=ord('0')) or \
            (ord(a_part[i])<=ord('f') and ord(a_part[i])>=ord('a')) or \
            (ord(a_part[i])<=ord('F') and ord(a_part[i])>=ord('A')):
            pass
        else:
            return False
    return True

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        find_v4=queryIP.find('.')
        find_v6=queryIP.find(':')
        if find_v4>=0 and find_v6>=0:
            return 'Neither'
        elif find_v4>=0:
            parts_list=queryIP.split('.')
            if len(parts_list)!=4:
                return 'Neither'
            for part in parts_list:
                if not is_valid_v4_part(part):
                    return 'Neither'
            return 'IPv4'
        elif find_v6>=0:
            parts_list=queryIP.split(':')
            if len(parts_list)!=8:
                return 'Neither'
            for part in parts_list:
                if not is_valid_v6_part(part):
                    return 'Neither'
            return 'IPv6'
        else:
            return 'Neither'
            
        
