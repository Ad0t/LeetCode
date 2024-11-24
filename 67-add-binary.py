'''
67. Add Binary
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
'''
class Solution(object):
    def addBinary(self, a, b):
        return format((int(''.join(str(a)), 2)+int(''.join(str(b)), 2)), 'b')