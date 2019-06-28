#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# https://leetcode.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (58.52%)
# Likes:    1763
# Dislikes: 28
# Total Accepted:    333.9K
# Total Submissions: 570.4K
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# Invert a binary tree.
# 
# Example:
# 
# Input:
# 
# 
# ⁠    4
# ⁠  /   \
# ⁠ 2     7
# ⁠/ \   / \
# 1   3 6   9
# 
# Output:
# 
# 
# ⁠    4
# ⁠  /   \
# ⁠ 7     2
# ⁠/ \   / \
# 9   6 3   1
# 
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
# 
# Google: 90% of our engineers use the software you wrote (Homebrew), but you
# can’t invert a binary tree on a whiteboard so f*** off.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
#class Solution:
#    def invertTree(self, root: TreeNode) -> TreeNode:
#        if root == None:
#            return None
#        self.invertOps(root)
#        return root
#        
#    def invertOps(self, root):
#        if root != None:
#            temp = root.right
#            root.right = root.left
#            root.left = temp
#        if root.left:
#            self.invertOps(root.left)
#        if root.right:
#            self.invertOps(root.right)
#        

# iterative
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        stack=[root]
        #stack.append(root)
        while stack != []:
            item = stack.pop(0)
            left = item.left
            if left!=None:
                stack.append(left)
            right = item.right
            if right !=None:
                stack.append(right)
            item.left = right
            item.right = left
        return root
