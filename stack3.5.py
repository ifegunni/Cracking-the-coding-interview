# Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.

class SortedStack:

    def __init__(self):
        self.stack = []
        self.sorted = []

    def enqueue(self, item):
        self.stack.append(item)

    def dequeue(self):
        if self.stack == []:
            return
        else:
            return self.stack.pop()

    def SortStack(self):
        if self.sorted == []:
            self.sorted.append(self.stack.pop())
        while self.stack != []:
            temp = self.stack.pop()
            while self.sorted != [] and temp < self.sorted[-1]:
                self.stack.append(self.sorted.pop())
            self.sorted.append(temp)

    def SortedPeek(self):
        return self.sorted[-1]

    def __str__(self):
        return str([self.stack, self.sorted])

    def isEmpty(self):
        return self.stack == []

x = SortedStack()

x.enqueue(5)
x.enqueue(6)
x.enqueue(3)
x.enqueue(4)
x.enqueue(7)
x.enqueue(8)
x.enqueue(9)
x.enqueue(10)
x.enqueue(1)
x.enqueue(2)
x.enqueue(3)
x.enqueue(4)
x.enqueue(5)

print(x)
x.SortStack()
print(x)
