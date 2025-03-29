"""
LeetCode 268: Missing Number
Difficulty: Easy
Link: https://leetcode.com/problems/missing-number/

Problem:
Given an array containing `n` distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

Example 1:
Input: nums = [3, 0, 1]
Output: 2

Example 2:
Input: nums = [0, 1]
Output: 2

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # 計算理想總和
        expected_sum = n * (n + 1) // 2
        # 計算實際總和
        actual_sum = sum(nums)
        # 差值即為缺失的數
        return expected_sum - actual_sum


def test():
    solution = Solution()
    assert solution.missingNumber([3, 0, 1]) == 2
    assert solution.missingNumber([0, 1]) == 2
    assert solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert solution.missingNumber([0]) == 1
    print("All tests passed!")

# 執行測試
if __name__ == "__main__":
    test()
