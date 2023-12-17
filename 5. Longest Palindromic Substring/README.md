# Longest Palindromic Substring

This repository contains a Python solution for the "Longest Palindromic Substring" problem on LeetCode.

## Problem Description

You can find the problem description [here](https://leetcode.com/problems/longest-palindromic-substring/description/).

## Solution

The solution is implemented in the `Solution` class in the `main.py` file. The `longestPalindrome` method takes a string `s` as input and returns the longest palindromic substring in `s`.

The solution works by adding special characters between the characters of the string, creating a modified string. It then uses the Manacher's algorithm to find the longest palindromic substring in the modified string. The algorithm maintains an array `p` to store the palindromic radii at each index. It iterates through the modified string, expanding palindromes around each index, updating the center and boundary of the current palindrome, and keeping track of the maximum length of palindrome and its center. Finally, it calculates the start and end indices of the maximum palindrome and returns the substring.

To use the solution, create an instance of the `Solution` class and call the `longestPalindrome` method with the input string. Here's an example:

```python
solution = Solution()
result = solution.longestPalindrome("input string")
print(result)
```

Make sure to replace `"input string"` with the actual string you want to find the longest palindromic substring in.