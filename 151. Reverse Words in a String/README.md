# LeetCode Problem: Reverse Words in a String

Link to the problem: [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150)

## Problem Description

Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

**Note:**
- The input string may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

## Example

```plaintext
Input: s = "the sky is blue"
Output: "blue is sky the"
```

## Explanation

This problem can be solved by splitting the input string `s` into individual words, reversing their order, and then joining them back together with a single space between each word.

The algorithm works as follows:
1. Split the input string `s` into individual words using the `split()` method.
2. Reverse the order of the words using slicing with `[::-1]`.
3. Join the reversed words back together into a single string using the `join()` method with a single space as the separator.

## Solution

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverse the order of the words in the input string `s`.

        :param s: Input string containing words separated by spaces.
        :return: String with words in reverse order concatenated by a single space.
        """
        return " ".join(s.split()[::-1])

# Example usage
if __name__ == '__main__':
    print(Solution().reverseWords("the sky is blue"))
```
