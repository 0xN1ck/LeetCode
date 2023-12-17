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