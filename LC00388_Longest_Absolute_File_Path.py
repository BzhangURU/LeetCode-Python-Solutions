# LC00388_Longest_Absolute_File_Path.py

# Suppose we have a file system that stores both files and directories. An example of one system 
# is represented in the following picture:



# Here, we have dir as the only directory in the root. dir contains two subdirectories, subdir1 
# and subdir2. subdir1 contains a file file1.ext and subdirectory subsubdir1. subdir2 contains 
# a subdirectory subsubdir2, which contains a file file2.ext.

# In text form, it looks like this (with ⟶ representing the tab character):

# dir
# ⟶ subdir1
# ⟶ ⟶ file1.ext
# ⟶ ⟶ subsubdir1
# ⟶ subdir2
# ⟶ ⟶ subsubdir2
# ⟶ ⟶ ⟶ file2.ext
# If we were to write this representation in code, it will look like this: 
# "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext". 
# Note that the '\n' and '\t' are the new-line and tab characters.

# Every file and directory has a unique absolute path in the file system, which is the order of 
# directories that must be opened to reach the file/directory itself, all concatenated by '/'s. 
# Using the above example, the absolute path to file2.ext is "dir/subdir2/subsubdir2/file2.ext". 
# Each directory name consists of letters, digits, and/or spaces. Each file name is of the form 
# name.extension, where name and extension consist of letters, digits, and/or spaces.

# Given a string input representing the file system in the explained format, return the length of 
# the longest absolute path to a file in the abstracted file system. If there is no file in the 
# system, return 0.

# Note that the testcases are generated such that the file system is valid and no file or directory 
# name has length 0.

 

# Example 1:


# Input: input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
# Output: 20
# Explanation: We have only one file, and the absolute path is "dir/subdir2/file.ext" of length 20.
# Example 2:


# Input: input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
# Output: 32
# Explanation: We have two files:
# "dir/subdir1/file1.ext" of length 21
# "dir/subdir2/subsubdir2/file2.ext" of length 32.
# We return 32 since it is the longest absolute path to a file.
# Example 3:

# Input: input = "a"
# Output: 0
# Explanation: We do not have any files, just a single directory named "a".
 

# Constraints:

# 1 <= input.length <= 104
# input may contain lowercase or uppercase English letters, a new line character '\n', 
# a tab character '\t', a dot '.', a space ' ', and digits.
# All file and directory names have positive length.

# Idea: split string with '\n', use a list to save each subfolder's name [root_folder_name, sub_folder_name, subsubfolder_name,... ] 

from collections import deque
def count_tabs__remove_tabs(line):
    count_tabs=0
    start_ind=0
    for i in range(len(line)):
        if line[i]=='\t':
            count_tabs+=1
        else:
            start_ind=i
            break
    return count_tabs, line[start_ind:]


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines=input.split('\n')

        list_each_level_folder_name=deque()
        result=0

        for line in lines:
            num_tab, line_without_tabs=count_tabs__remove_tabs(line)
            while len(list_each_level_folder_name)>num_tab:
                list_each_level_folder_name.pop()
            if line.find('.')>=0:
                # is a file
                path_length=0
                for folder_name in list_each_level_folder_name:
                    path_length+=len(folder_name)+1 #'/'
                path_length+=len(line_without_tabs)
                if path_length>result:
                    result=path_length
            else:
                #is a folder
                list_each_level_folder_name.append(line_without_tabs)
        return result


        



