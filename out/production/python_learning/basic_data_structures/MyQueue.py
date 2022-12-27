from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def dequeue(self):
        return self.buffer.pop()

    def enqueue(self, value):
        return self.buffer.appendleft(value)

    def front(self):
        return self.buffer[-1]

    def size(self):
        return len(self.buffer)

    def is_empty(self):
        return len(self.buffer) == 0

    def __repr__(self):
        return ' '.join(self.buffer)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)

    print(queue.dequeue())
