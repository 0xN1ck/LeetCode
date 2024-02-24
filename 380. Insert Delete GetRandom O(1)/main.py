import random


class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val not in self.val_to_index:
            self.vals.append(val)
            self.val_to_index[val] = len(self.vals) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.val_to_index:
            index = self.val_to_index[val]
            last_val = self.vals[-1]
            self.vals[index], self.val_to_index[last_val] = last_val, index
            self.vals.pop()
            del self.val_to_index[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.vals)


if __name__ == '__main__':
    obj = RandomizedSet()
    print('insert', obj.insert(2))
    print('insert', obj.insert(2))
    print('insert', obj.insert(5))
    print('remove', obj.remove(2))
    print('random', obj.getRandom())
    print('random', obj.getRandom())
    print('random', obj.getRandom())
