from typing import List


class Solution:
    def jump(self, nums: List[int]) -> bool:
        max_reachable = 0
        step = 0
        current_end = 0
        for i in range(len(nums) - 1):
            val = i + nums[i]
            max_reachable = max(max_reachable, val)

            if i == current_end:
                current_end = max_reachable
                step += 1

        return step


if __name__ == '__main__':
    print(Solution().jump([2, 0, 2, 0, 1]))
