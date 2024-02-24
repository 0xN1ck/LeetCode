# LeetCode Problem: Gas Station

Link to the problem: [Gas Station](https://leetcode.com/problems/gas-station/description/?envType=study-plan-v2&envId=top-interview-150)

## Problem Description

There are N gas stations along a circular route, where the amount of gas at station i is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

**Note:**

- If there exists a solution, it is guaranteed to be unique.
- Both input arrays are non-empty and have the same length.
- Each element in the input arrays is a non-negative integer.

## Explanation

This problem can be solved using a greedy approach. The idea is to start from each gas station and check if we can complete the circuit. If we can, we return the index of the starting gas station; otherwise, we return -1.

The algorithm works as follows:

1. If the total sum of gas is less than the total sum of cost, it means that there is no possible solution, so we return -1.

2. Initialize variables `total_gas` and `total_cost` to keep track of the total gas and total cost respectively. Also, initialize `start_station` to keep track of the starting gas station index and `current_gas` to keep track of the current gas in the tank.

3. Iterate through each gas station:
   - Increment `total_gas` by `gas[i]`.
   - Increment `total_cost` by `cost[i]`.
   - Update `current_gas` by adding `gas[i]` and subtracting `cost[i]`.
   - If `current_gas` becomes negative at any point, it means we can't complete the circuit starting from the current station. So, update `start_station` to the next station and reset `current_gas` to 0.

4. After iterating through all stations, if `total_gas` is greater than or equal to `total_cost`, it means there exists a solution. In this case, return `start_station`, otherwise return -1.

## Solution

```python
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total_gas = 0
        total_cost = 0
        start_station = 0
        current_gas = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_gas += gas[i] - cost[i]

            if current_gas < 0:
                start_station = i + 1
                current_gas = 0

        if total_gas >= total_cost:
            return start_station
        else:
            return -1

# Example usage
if __name__ == '__main__':
    print(Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
```
