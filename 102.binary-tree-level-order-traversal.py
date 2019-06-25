#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (48.84%)
# Likes:    1525
# Dislikes: 40
# Total Accepted:    388.7K
# Total Submissions: 795.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        result = []
        queue = [root, None]
        row = []
        while len(queue) > 0:
            item = queue.pop(0)
            if item != None:
                row.append(item.val)
                if item.left != None:
                    queue.append(item.left)
                if item.right != None:
                    queue.append(item.right)
            else:
                result.append(row)
                row = []
                # careful here, we add None
                # only when there is still node(Not None)
                # in queue
                if len(queue) > 0:
                    queue.append(None)
        return result





