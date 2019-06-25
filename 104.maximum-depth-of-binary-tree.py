#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (60.85%)
# Likes:    1354
# Dislikes: 54
# Total Accepted:    522.8K
# Total Submissions: 859K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its depth = 3.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        depth = 0
        queue = [root, None]
        while len(queue) > 0:
            item = queue.pop(0)
            if item == None:
                depth +=1
                if len(queue)>0:
                    queue.append(None)
            else:
                if item.left != None:
                    queue.append(item.left)
                if item.right != None:
                    queue.append(item.right)
        return depth





