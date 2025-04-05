class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        binarys = []

        for i in range(n + 1):
            ones = bin(i).count('1')
            binarys.append(ones)
        return binarys


def test():
    solution = Solution()
    assert solution.countBits(0) == [0]
    assert solution.countBits(1) == [0, 1]
    assert solution.countBits(2) == [0, 1, 1]
    assert solution.countBits(5) == [0, 1, 1, 2, 1, 2]
    assert solution.countBits(10) == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
    print("All tests passed!")

# 執行測試
if __name__ == "__main__":
    test()
