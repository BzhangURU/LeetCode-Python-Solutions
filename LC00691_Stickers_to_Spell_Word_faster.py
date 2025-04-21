# LC00691_Stickers_to_Spell_Word_faster.py: in recursion, when choosing stickers, only allow 
# index going higher, e.g.: choose 0,0,0,0,3,4,4,5, 
# 
# also, during recursion, 
# keeping  running remove_suboptimal_stickers (but don't touch stickers before cur sticker to avoid index error)
# slows speed down.

# We are given n different types of stickers. Each sticker has a lowercase English word on it.

# You would like to spell out the given string target by cutting individual letters from 
# your collection of stickers and rearranging them. You can use each sticker more than once 
# if you want, and you have infinite quantities of each sticker.

# Return the minimum number of stickers that you need to spell out target. 
# If the task is impossible, return -1.

# Note: In all test cases, all words were chosen randomly from the 1000 most common US 
# English words, and target was chosen as a concatenation of two random words.

 

# Example 1:

# Input: stickers = ["with","example","science"], target = "thehat"
# Output: 3
# Explanation:
# We can use 2 "with" stickers, and 1 "example" sticker.
# After cutting and rearrange the letters of those stickers, we can form the target "thehat".
# Also, this is the minimum number of stickers necessary to form the target string.
# Example 2:

# Input: stickers = ["notice","possible"], target = "basicbasic"
# Output: -1
# Explanation:
# We cannot form the target "basicbasic" from cutting letters from the given stickers.
 

# Constraints:

# n == stickers.length
# 1 <= n <= 50
# 1 <= stickers[i].length <= 10
# 1 <= target.length <= 15
# stickers[i] and target consist of lowercase English letters.

# We want to perform an exhaustive search, but we need to speed it up based on the input data being random. 
# For all stickers, we can ignore any letters that are not in the target word. When our candidate answer 
# won't be smaller than an answer we have already found, we can stop searching this path. When a sticker 
# dominates another, we shouldn't include the dominated sticker in our sticker collection. 
# [Here, we say a sticker `A` dominates `B` if `A.count(letter) >= B.count(letter)` for all letters.]

from typing import List
class Solution:
    def remove_suboptimal_stickers_and_sort(self,dict_letters_missing,stickers,start_index, sort=True):
        # only process elements after index: start_index
        flag_deleted_stickers=[0]*len(stickers)
        for i in range(start_index,len(stickers)):
            if flag_deleted_stickers[i]==0:
                for j in range(start_index,len(stickers)):
                    if i!=j:
                        keep_j=False
                        for k,v in dict_letters_missing.items():
                            # it is pointless to have more letter k than v because v is the final goal
                            if stickers[j].count(k)>stickers[i].count(k) and stickers[i].count(k)<v:
                                keep_j=True
                        if keep_j==False:
                            flag_deleted_stickers[j]=1
        new_stickers=[]
        for i in range(len(stickers)):
            if flag_deleted_stickers[i]==0:
                new_stickers.append(stickers[i])

        if sort:
            stickers_and_contributions_after_start_index=[]
            for i in range(start_index,len(new_stickers)):
                contribution=0
                if new_stickers[i]=='hope':
                    i=i
                for k,v in dict_letters_missing.items():
                    # it is pointless to have more letter k than v because v is the final goal
                    count=new_stickers[i].count(k)
                    if count>0:
                        contribution+=min(v,count)
                stickers_and_contributions_after_start_index.append((new_stickers[i],-contribution))
            stickers_and_contributions_after_start_index.sort(key=lambda p: p[1])
            for i in range(start_index,len(new_stickers)):
                new_stickers[i]=stickers_and_contributions_after_start_index[i-start_index][0]
        return new_stickers

    def it_is_possible_task(self,dict_letters_missing, stickers):
        set_letters=set()
        for i in range(len(stickers)):
            for letter_ind in range(len(stickers[i])):
                set_letters.add(stickers[i][letter_ind])
        for k,v in dict_letters_missing.items():
            if k not in set_letters:
                return False
        return True

    def recursion(self, dict_letters_missing, stickers, cur_best_list, cur_step, record_step):
        if record_step==[0,1]:#[0,0,1,1,2,3,4]:
            cur_step=cur_step
        if len(dict_letters_missing)==0:
            if cur_step<cur_best_list[0]:
                cur_best_list[0]=cur_step
        elif cur_step>=cur_best_list[0]:
            pass
        else:
            if len(record_step)==0:
                cur_index=0
            else:
                cur_index=record_step[-1]

            #if we set cur_index as start, then we can't call remove_suboptimal_stickers, as new_stickers will be changed
            # and index will be different with stickers
            for i in range(cur_index, len(stickers)):
                record_step.append(i)
                #save original dict
                original_dict=dict_letters_missing.copy()
                
                # make sure stickers[i] is still needed
                letters_sticker_i_contributes=0
                for k,v in dict_letters_missing.items():
                    count=stickers[i].count(k)
                    if count>0:
                        letters_sticker_i_contributes+=count
                        break
                if letters_sticker_i_contributes==0:
                    record_step.pop()
                    continue

                # dict - stickers[i]:
                for ind in range(len(stickers[i])):
                    if stickers[i][ind] in dict_letters_missing:
                        if dict_letters_missing[stickers[i][ind]]==1:
                            del dict_letters_missing[stickers[i][ind]]
                        else:
                            dict_letters_missing[stickers[i][ind]]-=1
                self.recursion(dict_letters_missing,stickers,cur_best_list,cur_step+1,record_step)

                dict_letters_missing=original_dict
                record_step.pop()

    def minStickers(self, stickers: List[str], target: str) -> int:
        dict_letters_missing={}
        for i in range(len(target)):
            if target[i] not in dict_letters_missing:
                dict_letters_missing[target[i]]=1
            else:
                dict_letters_missing[target[i]]+=1

        stickers=self.remove_suboptimal_stickers_and_sort(dict_letters_missing,stickers,0,True)
        #print(stickers)

        if not self.it_is_possible_task(dict_letters_missing, stickers):
            return -1
        
        cur_best_list=[len(target)]
        record_step=[]
        self.recursion(dict_letters_missing, stickers, cur_best_list, 0, record_step)
        return cur_best_list[0]

my_solu=Solution()
#stickers = ["bring","plane","should","against","chick"]
#target = "greatscore"

stickers = ["feed","industry","let","pair","milk","hope"]
target = "likehuman"
#['milk', 'industry', 'let', 'pair', 'hope']
#  1        1           0       1       1
# 0,1,3,4
print(my_solu.minStickers(stickers,target))
        
        


