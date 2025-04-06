class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


def test():
    solution = Solution()
    assert solution.climbStairs(2) == 2
    assert solution.climbStairs(5) == 8
    assert solution.climbStairs(6) == 13
    print("All tests passed!")


if __name__ == '__main__':
    test()