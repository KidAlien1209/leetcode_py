#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (54.50%)
# Likes:    2098
# Dislikes: 78
# Total Accepted:    479.6K
# Total Submissions: 879.5K
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Note:
# 
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
#
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        iModify=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[iModify]=nums[i]
                iModify+=1
        for j in range(iModify,len(nums)):
            nums[j]=0
        
