from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}

        for index, value in enumerate(nums):
            need_value = target - value

            if need_value in indexes:
                return [indexes[need_value], index]

            indexes[value] = index


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))