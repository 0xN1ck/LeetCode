class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]


if __name__ == '__main__':
    print(Solution().isPalindrome(-121))
