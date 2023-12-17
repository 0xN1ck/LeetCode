# Fibonacci Number

Solution for the "Fibonacci Number" problem on LeetCode.

## Problem

The Fibonacci numbers, commonly denoted as F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

```
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
```

Given n, calculate F(n).

## Solution

To solve this problem, we can use a recursive approach with memoization. We can define a function `fib()` that takes an integer `n` as input and returns the `n`th Fibonacci number.

We use the `@lru_cache` decorator from the `functools` module to cache the results of the function calls. This helps in memoizing the intermediate Fibonacci numbers and avoids redundant calculations.

In the `fib()` function, we handle the base cases where `n` is 0 or 1 and return the corresponding Fibonacci numbers. For any other value of `n`, we recursively calculate `F(n - 1)` and `F(n - 2)` using the `fib()` function and return their sum.

```python
from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
```

## Complexity Analysis

The time complexity of this solution is O(n) since we calculate each Fibonacci number once and store the results in the cache.

The space complexity is also O(n) since we use the cache to store the intermediate results.

## Links

- [Problem on LeetCode](https://leetcode.com/problems/fibonacci-number/)
- [Python functools module](https://docs.python.org/3/library/functools.html)