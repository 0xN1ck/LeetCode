from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        temp = nums[-k:]

        nums[k:] = nums[:-k]
        nums[:k] = temp

        print(nums)


if __name__ == '__main__':
    Solution().rotate([1, 2], 3)
