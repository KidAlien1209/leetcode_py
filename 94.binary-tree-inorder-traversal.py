#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (57.02%)
# Likes:    1669
# Dislikes: 72
# Total Accepted:    474K
# Total Submissions: 831K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        if root == None:
            return []
        self.inStack(stack, root)
        while stack != []:
            self.outStack(stack, result)
        return result

    def inStack(self, stack, node):
        cur = node
        stack.append(cur)
        while cur.left != None:
            stack.append(cur.left)
            cur = cur.left


    def outStack(self, stack, result):
        node = stack.pop()
        result.append(node.val)
        if node.right != None:
            self.inStack(stack, node.right)
        




