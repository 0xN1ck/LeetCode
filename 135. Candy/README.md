# Candy

## Problem Description

The problem titled [Candy](https://leetcode.com/problems/candy/description/?envType=study-plan-v2&envId=top-interview-150) is available on LeetCode. The task is to distribute candy to children based on their ratings.

### Explanation:

You are given an array `ratings`, where `ratings[i]` represents the rating of the `i-th` child. You need to give candy to these children according to the following requirements:

1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbors.

The goal is to minimize the total number of candies distributed.

## Solution

The Python solution for this problem is implemented in the `Solution` class. The `candy` method takes a list of integers `ratings` as input and returns an integer representing the minimum number of candies needed.

### Approach

1. Initialize two arrays `r_arr` and `l_arr` to keep track of candies distributed to the right and left neighbors respectively.
2. Start iterating through the ratings list from the second element.
3. For each element, compare its rating with the previous element to determine if it's higher or lower.
4. Based on the comparison, update the candies distributed to the current child in both directions.
5. Finally, sum up the maximum candies distributed to each child from both arrays.

#### Complexity Analysis

- Time complexity: O(n), where n is the length of the `ratings` list.
- Space complexity: O(n), where n is the length of the `ratings` list.

### Code Implementation

```python
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        last_give_r = 1
        last_give_l = 1
        r_arr = []
        l_arr = []
        r_arr.append(1)
        l_arr.append(1)
        rev_ratings = [i for i in ratings[::-1]]

        for i, (r, l) in enumerate(zip(ratings[1:], rev_ratings[1:]), start=1):
            if r > ratings[i - 1]:
                last_give_r += 1
                r_arr.append(last_give_r)
            else:
                last_give_r = 1
                r_arr.append(last_give_r)

            if l > rev_ratings[i - 1]:
                last_give_l += 1
                l_arr.append(last_give_l)
            else:
                last_give_l = 1
                l_arr.append(last_give_l)

        return sum(max(x, y) for x, y in zip(r_arr, l_arr[::-1]))

if __name__ == "__main__":
    print(Solution().candy([29, 51, 87, 87, 72, 12]))
```
