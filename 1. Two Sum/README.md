# Two Sum

[Link to the problem on LeetCode](https://leetcode.com/problems/two-sum/)

## Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

### Example:

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}

        for index, value in enumerate(nums):
            need_value = target - value

            if need_value in indexes:
                return [indexes[need_value], index]

            indexes[value] = index

if __name__ == "__main__":
    # Example usage
    print(Solution().twoSum([2, 7, 11, 15], 9))
