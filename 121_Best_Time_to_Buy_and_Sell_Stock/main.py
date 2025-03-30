class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 初始化最小價格為無窮大，最大利潤為 0
        min_price = float('inf')
        max_profit = 0

        # 一次遍歷 prices
        for price in prices:
            # 如果當前價格小於最小價格，更新 min_price
            if price < min_price:
                min_price = price
            # 如果賣出價格 - 買入價格大於目前最大利潤，更新 max_profit
            elif price - min_price > max_profit:
                max_profit = price - min_price

        # 返回最大利潤
        return max_profit


def test():
    solution = Solution()
    assert solution.maxProfit([7,1,5,3,6,4]) == 5
    assert solution.maxProfit([7,6,4,3,1]) == 0
    print("All tests passed!")

if __name__ == "__main__":
    test()