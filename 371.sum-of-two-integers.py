#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Easy (50.89%)
# Likes:    782
# Dislikes: 1373
# Total Accepted:    137.5K
# Total Submissions: 270.2K
# Testcase Example:  '1\n2'
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
# 
# 
# Example 1:
# 
# 
# Input: a = 1, b = 2
# Output: 3
# 
# 
# 
# Example 2:
# 
# 
# Input: a = -2, b = 3
# Output: 1
# 
# 
# 
# 
#
#class Solution:
#    def getSum(self, a: int, b: int) -> int:
#        a=int(a)
#        b=int(b)
#        if a==0:
#            return b
#        if b==0:
#            return a
#        return self.getSum((a^b), (a&b)<<1)
#
#if __name__ == "__main__":
#    a = Solution().getSum(-1,1)
#    print(a)

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        carry = 0
        result = 0
        mask = 1
        for i in range(32):
            a_bit = (a >> i) & mask
            b_bit = (b >> i) & mask
            res = a_bit ^ b_bit ^ carry
            carry = (a_bit&b_bit) | (a_bit&carry) | (b_bit&carry)
            result = result | (res << i)
        # Python has arbit long integers. If the last bit is 1, then we have a negative number in two's complement.
        # However, it will be treated as a positive number. Therefore, take the positive part out and remove -2**31
        # Another alternate way is to remove 2**32
        if result & 0x80000000: # 1 in bit number 32
            result = (result & 0x7fffffff) - 2**31
            #   result = result - 2**32 # Same thing as above
        return result   


