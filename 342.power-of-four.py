#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four/description/
#
# algorithms
# Easy (40.36%)
# Likes:    318
# Dislikes: 148
# Total Accepted:    116K
# Total Submissions: 287.1K
# Testcase Example:  '16'
#
# Given an integer (signed 32 bits), write a function to check whether it is a
# power of 4.
# 
# Example 1:
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 5
# Output: false
# 
# 
# Follow up: Could you solve it without loops/recursion?
#
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
    #    if num ==1:
    #        return True
    #    if num < 4:
    #        return False
    #    if num&(num-1)==0 and (num & 0x55555555)==num:
    #        return True
        if num==0:
            return False
        while num%4==0:
            num=num/4
        return num==1

