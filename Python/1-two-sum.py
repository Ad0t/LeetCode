'''
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''
class Solution(object):
    def twoSum(self, nums, target):
        # prevMap = {} #val : index
        # for index, number in enumerate(nums):
        #     diff = target - number
        #     if diff in prevMap:
        #         return [prevMap[diff], index]
        #     prevMap[number] = index
        # return
        prev = {}
        c = 0
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prev:
                return [prev[diff], i]
            prev[nums[i]] = i
        return