# LC00433_Minimum_Genetic_Mutation.py

# A gene string can be represented by an 8-character long string, 
# with choices from 'A', 'C', 'G', and 'T'.

# Suppose we need to investigate a mutation from a gene string startGene to a 
# gene string endGene where one mutation is defined as one single character changed in the gene string.

# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. 
# A gene must be in bank to make it a valid gene string.

# Given the two gene strings startGene and endGene and the gene bank bank, return 
# the minimum number of mutations needed to mutate from startGene to endGene. 
# If there is no such a mutation, return -1.

# Note that the starting point is assumed to be valid, so it might not be included in the bank.

 

# Example 1:

# Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1
# Example 2:

# Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2
 

# Constraints:

# 0 <= bank.length <= 10
# startGene.length == endGene.length == bank[i].length == 8
# startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].

from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene==endGene:
            return 0
        if len(bank)==0:
            return -1
        
        set_bank=set(bank)

        if endGene not in set_bank:
            return -1

        set_visited=set([startGene])

        my_q=deque()
        my_q.append(startGene)

        gene_type=['A','T','C','G']

        result=0

        while my_q:
            result+=1
            length_q=len(my_q)
            for i in range(length_q):
                cur_gene=my_q.popleft()
                cur_gene_list=list(cur_gene)
                for pos in range(8):
                    for gene_type_ind in range(4):
                        new_gene_list=cur_gene_list.copy()
                        new_gene_list[pos]=gene_type[gene_type_ind]
                        new_gene=''.join(new_gene_list)
                        if new_gene == endGene:
                            return result
                        if new_gene in set_bank and new_gene not in set_visited:
                            my_q.append(new_gene)
                            set_visited.add(new_gene)

        return -1

                         




