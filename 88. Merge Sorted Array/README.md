# Merge Sorted Array

Link to the problem: [LeetCode - Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/submissions/1183868398/?envType=study-plan-v2&envId=top-interview-150)

## Problem Description

Given two sorted integer arrays `nums1` and `nums2`, where `nums1` has a size `m + n`, with `m` elements already stored in it and the remaining `n` elements are set to 0, and `nums2` has `n` elements, merge `nums2` into `nums1` in sorted order.

## Python Solution

```python
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = sorted((nums1[:m] + nums2))
        for i in range(len(temp)):
            nums1[i] = temp[i]

if __name__ == '__main__':
    Solution().merge([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3)
```

## Explanation

- We define a class `Solution` containing the function `merge`.
- The function `merge` takes two sorted lists `nums1` and `nums2`, along with their sizes `m` and `n`.
- We create a temporary list `temp` by concatenating `nums1[:m]` and `nums2`, then sorting it.
- Then, we replace the elements of `nums1` with the elements of `temp`.
