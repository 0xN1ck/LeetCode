# Two Sum II - Input array is sorted

Link to the problem: [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150)

## Problem Description

Given an array of integers that is already sorted in ascending order, and a target integer `target`, find two numbers such that they add up to `target`. The function should return indices of the two numbers such that they add up to `target`, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

## Approach

To solve this problem, we can use the two-pointer technique combined with binary search.

1. Initialize two pointers, `left` and `right`, where `left` points to the beginning of the array and `right` points to the end of the array.

2. While `left` is less than `right`, compare the sum of the numbers at indices `left` and `right` with the target number.

3. If the sum is less than the target, increment `left` pointer.

4. If the sum is greater than the target, decrement `right` pointer.

5. If the sum is equal to the target, return indices `left + 1` and `right + 1`.

## Python Implementation

```python
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]

# Example usage
print(Solution().twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]
```
