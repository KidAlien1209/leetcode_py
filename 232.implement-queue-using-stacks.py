#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#
# https://leetcode.com/problems/implement-queue-using-stacks/description/
#
# algorithms
# Easy (43.61%)
# Likes:    571
# Dislikes: 110
# Total Accepted:    153.1K
# Total Submissions: 350.6K
# Testcase Example:  '["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement the following operations of a queue using stacks.
# 
# 
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# 
# 
# Example:
# 
# 
# MyQueue queue = new MyQueue();
# 
# queue.push(1);
# queue.push(2);  
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false
# 
# Notes:
# 
# 
# You must use only standard operations of a stack -- which means only push to
# top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may
# simulate a stack by using a list or deque (double-ended queue), as long as
# you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek
# operations will be called on an empty queue).
# 
# 
#
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack =[]
        self.helpStack=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.stack!=[]:
            self.helpStack.append(self.stack.pop())
        self.helpStack.append(x)
        while self.helpStack!=[]:
            self.stack.append(self.helpStack.pop())        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[-1]

        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

