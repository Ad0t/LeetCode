'''
796. Rotate String
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:
Input: s = "abcde", goal = "abced"
Output: false
'''
class Solution(object):
    def rotateString(self, s, goal):
        s = list(map(str, s))
        # print(s)
        r = ""
        for i in range(len(s)):
            el = s.pop()
            s.insert(0, el)
            r = "".join(s)
            print(r)
            if str(r) == goal:
                return True
        return False 