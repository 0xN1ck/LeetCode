# Palindrome Number

[Link to the problem on LeetCode](https://leetcode.com/problems/palindrome-number/)

## Description

Determine whether an integer `x` is a palindrome. An integer is a palindrome when it reads the same backward as forward.

### Example:

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]

if __name__ == '__main__':
    # Example usage
    print(Solution().isPalindrome(-121))
