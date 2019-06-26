#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (52.94%)
# Likes:    1712
# Dislikes: 152
# Total Accepted:    394.2K
# Total Submissions: 744K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# 
# 
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# 
#
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for item in nums:
            if count == 0:
                cand = item
                count +=1
            elif item == cand:
                count+=1
            else:
                count-=1
        return cand

