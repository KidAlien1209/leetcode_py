#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (35.93%)
# Likes:    857
# Dislikes: 51
# Total Accepted:    230.7K
# Total Submissions: 642K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example:
# 
# 
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next != None:
            next = cur.next
            if next.val == val:
                cur.next = next.next
            else:
                cur = cur.next

        return dummy.next


