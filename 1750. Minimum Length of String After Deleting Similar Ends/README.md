# 1750. Minimum Length of String After Deleting Similar Ends

## Problem Link
[1750. Minimum Length of String After Deleting Similar Ends](https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/?envType=daily-question&envId=2024-03-05)

## Problem Description
Given a string `s` consisting only of lowercase English letters, you can delete the same characters from both ends of the string until there are no characters that are the same on both ends.

Return the minimum length of the string after deleting the characters from the ends.

## Solution Explanation
The solution uses a two-pointer approach. The start and end pointers are initialized to point to the beginning and the end of the string s respectively. The while loop continues until the start pointer is less than the end pointer and the characters at the start and end pointers are the same.

Inside the while loop, the current character curr is set to the character at the start pointer. Then, the start and end pointers are moved towards the center of the string until they point to a character that is different from curr.

Finally, the function returns the difference between the end and start pointers plus one, which represents the minimum length of the string after deleting similar ends.

## Solution
```python
class Solution:
    def minimumLength(self, s: str) -> int:
        start = 0
        end = len(s)-1

        while start < end and s[start] == s[end]:
            curr = s[start]
            start += 1
            end -= 1
            while start <= end and s[start] == curr:
                start += 1
            while end >= start and s[end] == curr:
                end -= 1

        return end-start+1
