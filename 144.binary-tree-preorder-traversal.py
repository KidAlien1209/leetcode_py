#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (51.61%)
# Likes:    793
# Dislikes: 39
# Total Accepted:    346K
# Total Submissions: 670.4K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the preorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,2,3]
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        arr=[]
        result=[]
        if root == None:
            return []
        else:
            arr.append(root)
        while len(arr) != 0 :
            self.rec(arr.pop(), arr, result)
        return result

    def rec(self, root, arr, result):
        if root == None:
            return
        result.append(root.val)
        if root.right != None:
            arr.append(root.right)
        if root.left != None:
            arr.append(root.left)
        return


