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


print(Solution().minimumLength("aabccabba"))
