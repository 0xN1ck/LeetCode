# Jump Game II

Given an array of non-negative integers `nums`, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

**Example 1:**

Input: `nums = [2, 3, 1, 1, 4]`

Output: `2`

Explanation: The minimum number of jumps to reach the last index is `2`. Jump `1` step from index `0` to `1`, then `3` steps to the last index.

**Example 2:**

Input: `nums = [2, 0, 2, 0, 1]`

Output: `2`

Explanation: The minimum number of jumps to reach the last index is `2`. Jump `1` step from index `0` to `2`, then `2` steps to the last index.

**Constraints:**

- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 10^5`

## Approach

We can solve this problem using a greedy approach. At each step, we aim to maximize the reachable index using the current available jumps. We maintain three variables: `max_reachable`, `step`, and `current_end`. We iterate through the array, updating `max_reachable` with the maximum reachable index at each step. When the current index reaches `current_end`, we update `current_end` with `max_reachable`, indicating that a jump must be made. We increment `step` to count the number of jumps made.

## Implementation

```python
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reachable = 0
        step = 0
        current_end = 0
        for i in range(len(nums) - 1):
            val = i + nums[i]
            max_reachable = max(max_reachable, val)

            if i == current_end:
                current_end = max_reachable
                step += 1

        return step

if __name__ == '__main__':
    print(Solution().jump([2, 0, 2, 0, 1]))
```

This solution has a time complexity of O(n), where n is the length of the input array `nums`.