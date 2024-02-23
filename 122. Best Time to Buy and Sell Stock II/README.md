# Best Time to Buy and Sell Stock II

Link to the problem: [LeetCode - Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150)

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the i-th day. Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

## Python Solution

```python
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
```

## Explanation

- We define a class `Solution` containing the function `maxProfit`.
- The function `maxProfit` takes a list of integers `prices` representing the price of the stock on each day.
- We initialize the variable `profit` to 0.
- We iterate through the prices using a for loop and at each step, check if the price of the next day (`prices[j]`) is greater than the price of the current day (`prices[i]`). If it is, we add the difference to `profit`.
- Finally, we return the `profit`.