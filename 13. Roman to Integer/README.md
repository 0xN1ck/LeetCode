# Roman to Integer

[Link to the problem on LeetCode](https://leetcode.com/problems/roman-to-integer/)

## Description

Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M, which represent values 1, 5, 10, 50, 100, 500, and 1000 respectively.

Write a function that converts a Roman numeral to an integer.

### Example:

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        nums = [symbols[i] for i in s][::-1]
        result = 0
        last_num = 0
        for num in nums:
            if num >= last_num:
                result += num
            else:
                result -= num
            last_num = num
        return result

if __name__ == '__main__':
    # Example usage
    s = "MCMXCIV"
    print(Solution().romanToInt(s))
