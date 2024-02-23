from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices) - 1):
            j = i + 1

            if prices[j] > prices[i]:
                profit += (prices[j] - prices[i])

        return profit


if __name__ == '__main__':
    Solution().maxProfit([7, 1, 5, 3, 6, 4])
