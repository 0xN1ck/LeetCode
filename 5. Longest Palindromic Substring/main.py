class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Add special characters between the characters of the string
        modified_s = '#' + '#'.join(s) + '#'

        n = len(modified_s)
        p = [0] * n  # Array to store the palindromic radii
        C = R = 0  # Center and right boundary of the current palindrome
        max_len = 0  # Maximum length of palindrome
        center_index = 0  # Index of the center of the maximum palindrome

        for i in range(n):
            # Initialize the radius of the current palindrome
            p[i] = (R > i) and min(R - i, p[2 * C - i])

            # Expand the palindrome around the current index
            while i + 1 + p[i] < n and i - 1 - p[i] >= 0 and modified_s[i + 1 + p[i]] == modified_s[i - 1 - p[i]]:
                p[i] += 1

            # Update the center and boundary of the current palindrome
            if i + p[i] > R:
                C = i
                R = i + p[i]

            # Update the maximum length of palindrome and its center
            if p[i] > max_len:
                max_len = p[i]
                center_index = i

        # Calculate the start and end indices of the maximum palindrome
        start_index = (center_index - max_len) // 2
        end_index = start_index + max_len

        return str(s[start_index:end_index])
