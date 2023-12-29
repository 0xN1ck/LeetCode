from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recursive(nums, n):
            if n == 1:
                res.append(nums[:])
            else:
                for i in range(n):
                    recursive(nums, n-1)
                    if n % 2 == 0:
                        nums[i], nums[n-1] = nums[n-1], nums[i]
                    else:
                        nums[0], nums[n-1] = nums[n-1], nums[0]

        recursive(nums, len(nums))
        print(res)


if __name__ == "__main__":
    sol = Solution()
    sol.permute([1, 2, 3])
