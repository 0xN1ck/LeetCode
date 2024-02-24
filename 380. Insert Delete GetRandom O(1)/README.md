# LeetCode Problem: Insert Delete GetRandom O(1)

## Problem Description

You are required to design a data structure that supports the following operations in average O(1) time:

1. `insert(val)`: Inserts an item `val` into the set if it's not already present.
2. `remove(val)`: Removes an item `val` from the set if it exists.
3. `getRandom()`: Returns a random element from the set. Each element must have the same probability of being returned.

**Constraints:**

- `val` will always be non-negative.
- Each element in the set must be unique.

## Example

```plaintext
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 into the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 into the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always returns 2.
randomSet.getRandom();
```

## Approach

To achieve the required time complexities for `insert`, `remove`, and `getRandom` operations, we can use a combination of a dictionary (`val_to_index`) to store the values and their indices, and a list (`vals`) to store the values themselves. This approach allows us to perform all operations in O(1) time on average.

- For `insert(val)`, we check if `val` is already present in the set using `val_to_index`. If not, we append it to the `vals` list and store its index in `val_to_index`.
- For `remove(val)`, we check if `val` is present in the set using `val_to_index`. If it is, we swap `val` with the last element in `vals` and update the index of the last element accordingly. Then we remove `val` from `vals` and `val_to_index`.
- For `getRandom()`, we simply return a random element from `vals` using `random.choice()`.

## Implementation

```python
import random

class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val not in self.val_to_index:
            self.vals.append(val)
            self.val_to_index[val] = len(self.vals) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.val_to_index:
            index = self.val_to_index[val]
            last_val = self.vals[-1]
            self.vals[index], self.val_to_index[last_val] = last_val, index
            self.vals.pop()
            del self.val_to_index[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.vals)

# Example usage
if __name__ == '__main__':
    obj = RandomizedSet()
    print('insert', obj.insert(2))
    print('insert', obj.insert(2))
    print('insert', obj.insert(5))
    print('remove', obj.remove(2))
    print('random', obj.getRandom())
    print('random', obj.getRandom())
    print('random', obj.getRandom())
```