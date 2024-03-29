#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (48.84%)
# Likes:    919
# Dislikes: 46
# Total Accepted:    265.8K
# Total Submissions: 544.1K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
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
# Output: [3,2,1]
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        if root == None:
            return []
        self.inStack(root, stack)
        while len(stack) >0: 
            result.append(stack.pop().val)
        return result
    def inStack(self, node, stack):
        stack.append(node)
        if node.right != None:
            self.inStack(node.right, stack)
        if node.left != None:
            self.inStack(node.left, stack)
    
        


