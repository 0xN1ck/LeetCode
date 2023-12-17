# Print in Order

Solution for the "Print in Order" problem on LeetCode.

## Problem

Given a class `Foo` with three methods: `first()`, `second()`, and `third()`. Three threads call these methods asynchronously. It is guaranteed that `first()` will be called before `second()`, and `second()` will be called before `third()`.

Implement a mechanism to ensure that the methods are called in the order `first()` -> `second()` -> `third()`.

## Solution

To solve this problem, we can use semaphores to synchronize the execution of the methods. We can use two semaphores, `semaphore1` and `semaphore2`, to control the order of execution of the `first()` and `second()` methods.

In the `first()` method, we call `printFirst()` and then release `semaphore1` to allow the execution of the `second()` method.

In the `second()` method, we first wait until `semaphore1` is released, and then we call `printSecond()` and release `semaphore2` to allow the execution of the `third()` method.

In the `third()` method, we first wait until `semaphore2` is released, and then we call `printThird()`.

```python
from threading import Semaphore

class Foo:
    def __init__(self):
        self.semaphore1 = Semaphore(0)
        self.semaphore2 = Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.semaphore1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.semaphore1.acquire()
        printSecond()
        self.semaphore2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.semaphore2.acquire()
        printThird()
```

## Links

- [Problem on LeetCode](https://leetcode.com/problems/print-in-order/)
- [Python threading module](https://docs.python.org/3/library/threading.html)