#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (31.25%)
# Likes:    5395
# Dislikes: 1386
# Total Accepted:    911.8K
# Total Submissions: 2.9M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode(0)
        cur = dummy
        noop = ListNode(0)
        while l1!=None or l2!=None:
            val = (l1 or noop).val+(l2 or noop).val+carry
            cur.next = ListNode(val%10)
            if val>=10:
                carry=1
            else:
                carry=0
            l1=(l1 or noop).next
            l2=(l2 or noop).next
            cur=cur.next
        if carry==1:
            cur.next=ListNode(1)
        return dummy.next
            

