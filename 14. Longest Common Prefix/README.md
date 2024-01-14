# Longest Common Prefix

[Link to the problem on LeetCode](https://leetcode.com/problems/longest-common-prefix/)

## Description

Write a function to find the longest common prefix string amongst an array of strings.

## Solution

The provided Python solution uses a simple approach to find the longest common prefix. It compares characters at the same index in the words and builds the common prefix iteratively.

```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Uncomment the line below for a simpler solution using os.path.commonprefix
        # return os.path.commonprefix(strs)
        
        min_word = min(strs)
        prefix = ""
        id = 0
        for char in min_word:
            temp = ""
            for word in strs:
                if word[id] == char:
                    temp += char
                    if len(temp) == len(strs):
                        prefix += temp[0]
                        temp = ""
                        id += 1
                    continue
                else:
                    return prefix
        return prefix

if __name__ == "__main__":
    # Example usage
    print(Solution().longestCommonPrefix(["ab", "a"]))  # Output: "a"