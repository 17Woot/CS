class queue(object):
    def __init__(self, mSize):
        self.queue = list()
        self.maxsize = mSize
        self.top = 0

    def enqueue(self, data):
        if self.top >= self.maxsize:
            return False
        else:
            self.queue.append(data)
            self.top += 1
            return True

    def dequeue(self):
        if self.top <= 0:
            return False
        else:
            item = self.queue.pop(0)
            self.top -= 1
            return item

    def peek(self):
        if self.top <= 0:
            return False
        else:
            return self.queue[self.top - 1]

    def isEmpty(self):
        if self.top <= 0:
            return True
        else:
            return False

    def isFull(self):
        if self.top >= self.maxsize:
            return True
        else:
            return False

    def show(self):
        return self.queue

if __name__ == "__main__":
    q = queue(20)
    q.enqueue(3)
    q.enqueue("hello world")
    q.enqueue("hello world")
    q.enqueue("world hello")
    q.dequeue()
    print(q.show())

