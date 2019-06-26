#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Easy (37.37%)
# Likes:    1846
# Dislikes: 194
# Total Accepted:    310.9K
# Total Submissions: 831K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
# 
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# 
# 
# 
# 
# Example:
# 
# 
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
# 
# 
# 
# 
#
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minVal = float('-inf')
        self.stack = []

        

    def push(self, x: int) -> None:
        if self.stack == []:
            self.minVal=x
            self.stack.append(0)
            return
        d = x - self.minVal
        self.stack.append(d)
        if d < 0:
            self.minVal = x

    def pop(self) -> None:
        item = self.stack.pop()
        if item < 0:
            self.minVal = self.minVal - item
        
    def top(self) -> int:
        topItem = self.stack[-1]
        if topItem<=0:
            topVal = self.minVal
        else:
            topVal = self.minVal + topItem
        return topVal

    def getMin(self) -> int:
        return self.minVal
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

