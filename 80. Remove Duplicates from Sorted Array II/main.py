from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        j = 0
        for i in range(len(nums)):
            if nums[i - 2 - j] == nums[i - 1 - j] == nums[i - j]:
                nums.pop(i - j)
                nums.append('_')
                j += 1

        return len(nums[:-j]) if j > 0 else len(nums)


if __name__ == '__main__':
    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
