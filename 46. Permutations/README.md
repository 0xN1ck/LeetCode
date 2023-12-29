# 46. Permutations

## Problem Description

Given a collection of distinct integers, return all possible permutations.

**Example:**

```plaintext
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

## Solution

The solution involves generating all permutations of the given list of distinct integers. The algorithm (Heap's Algorithm) uses a recursive approach to explore all possible arrangements of the elements. It swaps elements in the list during the recursive calls to generate different permutations.

The `permute` function takes a list of integers as input and returns a list of all possible permutations.

```python
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recursive(nums, n):
            if n == 1:
                res.append(nums[:])
            else:
                for i in range(n):
                    recursive(nums, n-1)
                    if n % 2 == 0:
                        nums[i], nums[n-1] = nums[n-1], nums[i]
                    else:
                        nums[0], nums[n-1] = nums[n-1], nums[0]

        recursive(nums, len(nums))
        return res

if __name__ == "__main__":
    sol = Solution()
    result = sol.permute([1, 2, 3])
    print(result)
```

The `permute` function initializes an empty list `res` to store the permutations. It then calls the `recursive` helper function to generate permutations. The `recursive` function performs the following steps:

- If `n` is 1, the current arrangement of elements is a permutation, so it is added to the result list.
- Otherwise, the function uses a loop to iterate through the elements and recursively generate permutations for the remaining elements.
- Swapping elements is done based on whether `n` is even or odd.

Finally, the main block demonstrates how to use the `Solution` class to find permutations for the given example `[1, 2, 3]`. The result is printed to the console.