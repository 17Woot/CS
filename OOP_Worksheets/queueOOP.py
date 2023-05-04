# Circular Queue
# Must remember to reset tail and head to 0 when they reach the end of the queue
class Queue(object):
    def __init__(self, msize):
        self.__head = 0
        self.__tail = 0
        self.size = msize
        self.__queue = list()
        while len(self.__queue) < msize:
            self.__queue.append("") # Fill the queue with empty strings

    def isEmpty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def isFull(self):
        if self.head == 0 and self.tail == self.size-1:
            return True
        elif self.head == self.tail + 1:
            return True
        else:
            return False

    def enqueue(self, data):
        if self.isFull():
            return False
        else:
            self.__queue[self.__tail] = data
            if self.__tail == self.size:
                self.tail = 0
            else:
                self.tail += 1
            return True

    def dequeue(self):
        if self.isEmpty():
            return False
        else:
            item = self.__queue[self.__head]
            if self.__head == self.size:
                self.head = 0
            else:
                self.head += 1
            return item

    def get_queue(self):
        return self.__queue



if __name__ == "__main__":
  pass

