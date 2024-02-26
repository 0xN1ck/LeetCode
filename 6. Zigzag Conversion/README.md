# ZigZag Conversion

## Problem Description
The problem can be found on [LeetCode](https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150).

The ZigZag Conversion problem involves transforming a given string into a zigzag pattern and returning the resulting string when read line-by-line. Given a string `s` and a number of rows `numRows`, the task is to arrange the characters of the string in a zigzag pattern and return the final string.


## Approach
To solve this problem, we can follow these steps:

1. Create an array of strings, where each string represents a row in the zigzag pattern.
2. Iterate over the input string, determining the index of the row where each character should be placed.
3. Keep track of the current row and the direction in which we are moving (up or down the rows).
4. Once all characters are added to the rows, join the letters of the separate arrays to make strings, and then join those strings to create the final zigzag string.

## Example
Let's take an example to illustrate the approach. Suppose we have the input string `"ABCDEFGH"` and the number of rows is 3. The zigzag pattern would look like this:

```
A   E   G
B D F H
C
```

Taking the lines of the arrays away (essentially converting these arrays to strings), we get three strings: `"AEG"`, `"BDFH"`, and `"C"`. Adding them together, line by line, we get the result: `"AEBDFHCG"`.

## Implementation
Here's the Python implementation of the solution:

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = [[] for _ in range(numRows)]
        if numRows == 1:
            arr.append(s)
            return ''.join([''.join(i) for i in arr])

        revers = False
        step = 0

        for index, syb in enumerate(s):
            if not revers:
                arr[step].append(syb)
                step += 1
            else:
                step -= 1
                arr[step].append(syb)

            if step == numRows:
                step -= 1
                revers = True
            if step == 0:
                step += 1
                revers = False

        return ''.join([''.join(i) for i in arr])

if __name__ == '__main__':
    solution = Solution()
    result = solution.convert('PAYPALISHIRING', 4)
    print(result)  # Output: "PINALSIGYAHRPI"
```
