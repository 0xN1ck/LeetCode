# Jump Game

Link to the problem: [LeetCode - Jump Game](https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150)

## Problem Description

Given an array of non-negative integers `nums`, where each element represents the maximum jump length at that position, determine if you can reach the last index.

## Python Solution

```python
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        for i, jump in enumerate(nums):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + jump)

        return True

if __name__ == '__main__':
    print(Solution().canJump([2, 3, 1, 1, 4]))
    print(Solution().canJump([3, 2, 1, 0, 4]))
```

## Explanation

- We define a class `Solution` containing the function `canJump`.
- The function `canJump` takes a list of non-negative integers `nums` representing the maximum jump length at each position.
- We initialize `max_reachable` to 0, which represents the maximum index we can reach.
- We iterate through the `nums` list using `enumerate` to get both the index `i` and the jump length `jump`.
- If the current index `i` is greater than `max_reachable`, it means we cannot reach the current position, so we return `False`.
- Otherwise, we update `max_reachable` to be the maximum of its current value and `i + jump`, which represents the farthest index we can reach from the current position.
- If we successfully iterate through the entire `nums` list without encountering a position we cannot reach, we return `True`.
