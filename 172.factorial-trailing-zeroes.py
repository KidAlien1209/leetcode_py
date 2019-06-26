#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (37.41%)
# Likes:    487
# Dislikes: 706
# Total Accepted:    159.6K
# Total Submissions: 426.7K
# Testcase Example:  '3'
#
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Example 1:
# 
# 
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# 
# Example 2:
# 
# 
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# 
# Note: Your solution should be in logarithmic time complexity.
# 
#
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        result=0
        factor = 1
        while pow(5,factor) <= n:
            factor+=1
        for i in range(1,factor):
            result += n // pow(5,i)
        return result

