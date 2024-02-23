from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = sorted((nums1[:m] + nums2))
        for i in range(len(temp)):
            nums1[i] = temp[i]


if __name__ == '__main__':
    Solution().merge([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3)
