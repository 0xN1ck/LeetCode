class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = [[] for i in range(numRows)]
        if numRows == 1:
            arr.append(s)
            print(''.join([''.join(i) for i in arr]))
            return ''.join([''.join(i) for i in arr])
        revers = False
        step = 0
        for index, syb in enumerate(s):
            if not revers:
                arr[step].append(syb)
                step += 1
            else:
                step -= 1
                arr[step].append(syb)
            if step == numRows:
                step -= 1
                revers = True
            if step == 0:
                step += 1
                revers = False

        return ''.join([''.join(i) for i in arr])

if __name__ == '__main__':
    Solution().convert('PAYPALISHIRING', 4)
