# Best Time to Buy and Sell Stock

## Problem Description

The problem titled [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150) is available on LeetCode. The task is to find the maximum profit that can be obtained by buying and selling a single share on a given day. 

### Example:
```python
Input: [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

## Solution

The Python solution for this problem is implemented in the `Solution` class. The `maxProfit` method takes a list of integers `prices` as input and returns an integer representing the maximum profit that can be achieved.

### Approach

1. Initialize variables `buy` and `max_profit` to track the buying price and maximum profit.
2. Iterate through the list of prices, starting from the second element.
3. Update `buy` to the minimum of current `buy` and the current price.
4. Calculate the profit by subtracting the buying price from the current price.
5. Update `max_profit` if the calculated profit is greater than the current `max_profit`.
6. Return the `max_profit`.

#### Complexity Analysis

- Time complexity: O(n), where n is the length of the `prices` list.
- Space complexity: O(1), constant space is used.

### Code Implementation

```python
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
```
