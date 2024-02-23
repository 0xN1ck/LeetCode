# Rotate Array

Link to the problem: [LeetCode - Rotate Array](https://leetcode.com/problems/rotate-array/submissions/1183914802/?envType=study-plan-v2&envId=top-interview-150)

## Problem Description

Given an array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

## Python Solution

```python
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        temp = nums[-k:]

        nums[k:] = nums[:-k]
        nums[:k] = temp

        print(nums)

if __name__ == '__main__':
    Solution().rotate([1, 2], 3)
```

## Explanation

- We define a class `Solution` containing the function `rotate`.
- The function `rotate` takes a list of integers `nums` and an integer `k`.
- We first handle the case where `k` is greater than the length of `nums` by taking the modulo of `k` with the length of `nums`.
- Then, we create a temporary list `temp` containing the last `k` elements of `nums`.
- We update `nums` by assigning the slice of `nums` from index `k` to the end to be the elements from the beginning to index `-k` (excluding `-k`).
- Similarly, we assign the slice of `nums` from the beginning to index `k` to be the elements from `temp`.
- Finally, we print the modified `nums`.
