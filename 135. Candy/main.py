from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        last_give = 1
        total_give = 0
        for index, rating in enumerate(ratings):
            if index == 0:
                if rating <= ratings[index + 1]:
                    total_give += last_give
                else:
                    total_give += last_give + 1
                continue

            if index == len(ratings) - 1:
                if rating <= ratings[index - 1]:
                    last_give = 1
                    total_give += last_give
                else:
                    total_give += last_give + 1
                break

            if rating >= ratings[index - 1]:
                last_give += 1
                total_give += last_give
            else:
                last_give = 1
                total_give += last_give

        return total_give


if __name__ == "__main__":
    # print(Solution().candy([1, 0, 2]))
    # print(Solution().candy([1, 2, 2]))
    print(Solution().candy([29, 51, 87, 87, 72, 12]))
    print((Solution().candy([1, 2, 87, 87, 87, 2, 1])))
