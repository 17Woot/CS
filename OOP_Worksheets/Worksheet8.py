class MyStack(object):
    def __init__(self, mSize):
        self.stack = list()
        self.maxsize = mSize
        self.top= 0

    def push(self, data):
        if self.top >= self.maxsize:
            return False
        else:
            self.stack.append(data)
            self.top += 1
            return True
    def pop(self):
        if self.top<=0:
            return False
        else:
            item = self.stack.pop()
            self.top -= 1
            return item

    def peek(self):
        if self.top<=0:
            return False
        else:
            return self.stack[self.top-1]

    def isEmpty(self):
        if self.top<=0:
            return True
        else:
            return False

    def isFull(self):
        if self.top>=self.maxsize:
            return True
        else:
            return False

    def show(self):
        return self.stack


if __name__ == "__main__":
    s = MyStack(108)
    s.push(3)
    s.push("hello world")
    print(s.show())
    print(s.pop())
    print(s.show())
    for n in range (0,105):
        s.push(n)
    print(s.show())
    print(s.isFull())
    s.push(100)
    s.push("hello world")
    s.push("hola")
    s.push("hoi")
    print(s.isFull())
