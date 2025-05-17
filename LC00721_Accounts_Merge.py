# LC00721_Accounts_Merge.py

# Given a list of accounts where each element accounts[i] is a list of strings, 
# where the first element accounts[i][0] is a name, and the rest of the elements 
# are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the 
# same person if there is some common email to both accounts. Note that even if two 
# accounts have the same name, they may belong to different people as people could 
# have the same name. A person can have any number of accounts initially, but all 
# of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first 
# element of each account is the name, and the rest of the elements are emails in 
# sorted order. The accounts themselves can be returned in any order.

 

# Example 1:

# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
#                    ["John","johnsmith@mail.com","john00@mail.com"],
#                    ["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
#          ["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and second John's are the same person as they have the common email "johnsmith@mail.com".
# The third John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], 
#                                                                   ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
# Example 2:

# Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
#                    ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
#                    ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
#                    ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
#                    ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
# Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
#          ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
#          ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
#          ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
#          ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
 

# Constraints:

# 1 <= accounts.length <= 1000
# 2 <= accounts[i].length <= 10
# 1 <= accounts[i][j].length <= 30
# accounts[i][0] consists of English letters.
# accounts[i][j] (for j > 0) is a valid email.

from typing import List

#Idea: create a dictionary that maps email to account id. For new account, check all emails with dict. 
#Be careful! You may have email1, email2 in account0, email3, email4 in account1, looks separate, but later, you have email 
# email 2 and email3 in another account, then you need to merge them all. 

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dict_email_to_id={}
        result_accounts=[]

        for i in range(len(accounts)):
            matched_id=set()
            account=accounts[i]
            for j in range(1,len(account)):
                email=account[j]
                if email in dict_email_to_id:
                    matched_id.add(dict_email_to_id[email])
                
            if len(matched_id)==0:
                result_accounts.append([account[0]])
                account_id=len(result_accounts)-1

                for j in range(1,len(account)):
                    email=account[j]
                    if email not in dict_email_to_id:
                        dict_email_to_id[email]=account_id
                        result_accounts[-1].append(email)
            else:
                #change matched_id to sorted list
                list_matched_id=[]
                for item in matched_id:
                    list_matched_id.append(item)

                list_matched_id.sort(reverse=True)

                smallest_id=list_matched_id[-1]

                for j in range(1,len(account)):
                    email=account[j]

                    if email not in dict_email_to_id:
                        result_accounts[smallest_id].append(email)
                        dict_email_to_id[email]=smallest_id

                for i in range(len(list_matched_id)-1):
                    extra_account_id=list_matched_id[i]
                    for j in range(1,len(result_accounts[extra_account_id])):
                        result_accounts[smallest_id].append(result_accounts[extra_account_id][j])
                        dict_email_to_id[result_accounts[extra_account_id][j]]=smallest_id
                    result_accounts[extra_account_id]=[]#we can't delete it, as it will disturb the index of other accounts
        result=[]

        for i in range(len(result_accounts)):
            if len(result_accounts[i])>0:
                result_accounts[i][1:] = sorted(result_accounts[i][1:])
                result.append(result_accounts[i])

        return result
        
accounts=[["Hanzo","Hanzo2@m.co","Hanzo3@m.co"],["Hanzo","Hanzo4@m.co","Hanzo5@m.co"],
          ["Hanzo","Hanzo0@m.co","Hanzo1@m.co"],["Hanzo","Hanzo3@m.co","Hanzo4@m.co"],
          ["Hanzo","Hanzo7@m.co","Hanzo8@m.co"],["Hanzo","Hanzo1@m.co","Hanzo2@m.co"],
          ["Hanzo","Hanzo6@m.co","Hanzo7@m.co"],["Hanzo","Hanzo5@m.co","Hanzo6@m.co"]]
my_solu=Solution()
my_solu.accountsMerge(accounts)

