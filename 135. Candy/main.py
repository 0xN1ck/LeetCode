from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        last_give_r = 1
        last_give_l = 1
        r_arr = []
        l_arr = []
        r_arr.append(1)
        l_arr.append(1)
        rev_ratings = [i for i in ratings[::-1]]

        for i, (r, l) in enumerate(zip(ratings[1:], rev_ratings[1:]), start=1):
            if r > ratings[i - 1]:
                last_give_r += 1
                r_arr.append(last_give_r)
            else:
                last_give_r = 1
                r_arr.append(last_give_r)

            if l > rev_ratings[i - 1]:
                last_give_l += 1
                l_arr.append(last_give_l)
            else:
                last_give_l = 1
                l_arr.append(last_give_l)

        return sum(max(x, y) for x, y in zip(r_arr, l_arr[::-1]))


if __name__ == "__main__":
    print(Solution().candy([29, 51, 87, 87, 72, 12]))
