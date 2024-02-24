from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0

        for i in range(len(prices) - 1):
            if buy > prices[i]:
                buy = prices[i]
            profit = prices[i + 1] - buy
            if profit > max_profit:
                max_profit = profit

        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
