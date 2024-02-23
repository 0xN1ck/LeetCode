# Remove Duplicates from Sorted Array II

Link to the problem: [LeetCode - Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150)

## Problem Description

Given a sorted array `nums`, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

**Clarification:**
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller.

Internally, you can think of this:

```python
# nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

# any modification to nums in your function would be known by the caller.
# using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

### Example 1:

**Input:**
```python
nums = [1,1,1,2,2,3]
```

**Output:**
```python
5, nums = [1,1,2,2,3]
```

**Explanation:**
Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2, and 3 respectively. It doesn't matter what you leave beyond the returned length.

### Example 2:

**Input:**
```python
nums = [0,0,1,1,1,1,2,3,3]
```

**Output:**
```python
7, nums = [0,0,1,1,2,3,3]
```

**Explanation:**
Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3, and 3 respectively. It doesn't matter what values are set beyond the returned length.

## Solution Explanation

The solution involves iterating through the array and using two pointers to keep track of the elements. We maintain a count of the duplicates encountered for each element. If the count exceeds 2, we remove the duplicate by popping it from the list and appending a placeholder character ('_'). This process continues until the end of the array.

## Python Solution

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        j = 0
        for i in range(len(nums)):
            if nums[i - 2 - j] == nums[i - 1 - j] == nums[i - j]:
                nums.pop(i - j)
                nums.append('_')
                j += 1
        return len(nums[:-j]) if j > 0 else len(nums)

if __name__ == '__main__':
    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
```

## Explanation

- We define a class `Solution` that contains the function `removeDuplicates`.
- The function `removeDuplicates` takes in a list of integers `nums` and returns an integer.
- We handle the case where the length of `nums` is less than 3 by simply returning its length.
- We then initialize a counter `j` to 0.
- We iterate through the elements of `nums` using a for loop.
- Within the loop, we check if the current element is equal to the two previous elements.
- If it is, we pop the current element from `nums` and append a placeholder character ('_'). We also increment the counter `j`.
- Finally, we return the length of `nums` excluding the elements removed due to duplicates.
