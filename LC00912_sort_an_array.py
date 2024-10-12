# LC00912: sort an array

# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessarily unique.
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104


def sortArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    mergeSortLR(nums,0,len(nums))
    return nums

def mergeSortLR(nums, l, r):
    if l>=r-1:
        return
    m=(l+r)//2
    mergeSortLR(nums,l,m)
    mergeSortLR(nums,m,r)
    merge(nums,l,m,r)
    
    
def merge(nums,l,m,r):
    i=j=0
    k=l
    list1=nums[l:m]
    list2=nums[m:r]
    while i<m-l and j<r-m:
       if list1[i]<list2[j]:
           nums[k]=list1[i]
           k+=1
           i+=1
       else:
           nums[k]=list2[j]
           k+=1
           j+=1
    if i<m-l:
        while i<m-l:
            nums[k]=list1[i]
            k+=1
            i+=1
    else:
        while j<r-m:
            nums[k]=list2[j]
            k+=1
            j+=1
    


def printList(array):
    for i in range(len(array)):
        print(f"{array[i]}")

if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]
    #array[1:2]=[33,44]
    sortArray(array)

    print("Sorted array is: ")
    printList(array)
