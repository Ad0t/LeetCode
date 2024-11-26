'''
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        maxLen = 0
        charIdx = [-1] * 128
        left = 0

        for r in range(n):
            if charIdx[ord(s[r])] >= left:
                left = charIdx[ord(s[r])] + 1
            charIdx[ord(s[r])] = r
            maxLen = max(maxLen, r - left + 1)
        return maxLen