from typing import List
# from os.path import commonprefix # this is simple solving


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # return commonprefix(strs) # this is simple solving
        min_word = min(strs)
        prefix = ""
        id = 0
        for char in min_word:
            temp = ""
            for word in strs:
                if word[id] == char:
                    temp += char
                    if len(temp) == len(strs):
                        prefix += temp[0]
                        temp = ""
                        id += 1
                    continue
                else:
                    return prefix
        return prefix


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["ab", "a"]))