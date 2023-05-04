class Stack(object):
    def __init__(self, mSize):
        self.__stack = list()
        self.maxsize = mSize
        self.__sp = 0
        while len(self.__stack)<mSize:
            self.__stack.append("")

    def isEmpty(self):
        if self.__sp == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.__sp == self.maxsize:
            return True
        else:
            return False

    def push(self, data):
        if self.isFull():
            return False
        else:
            self.__stack[self.__sp] = data
            self.__sp += 1
            return True

    def pop(self):
        if self.isEmpty():
            return False
        else:
            item = self.__stack[self.__sp-1]
            self.__sp -= 1
            return item

    def get_sp(self):
        return self.__sp

    def get_stack(self):
        return self.__stack




if __name__ == "__main__":
    myStack = Stack(10)
    myStack.push(3)
    myStack.push("hello world")
    print(myStack.get_stack())
    print(myStack.pop())
    myStack.push(1)
    print(myStack.get_stack())
