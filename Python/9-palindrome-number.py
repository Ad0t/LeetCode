'''
9. Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''
class Solution(object):
    def isPalindrome(self, x):
        # if x < 0: return False
        # div = 1
        # while x >= 10 * div:
        #     div *= 10
        # while x:
        #     right = x % 10
        #     left = x // div
        #     if left != right: return False
        #     x = (x % div) // 10
        #     div /= 100
        # return True
        # if x < 0:
        #     return False
        x = list(str(x))
        if x[::-1] != x[::]:
            return False
        return True