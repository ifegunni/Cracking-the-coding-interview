#Queue via Stack: Implement a MyQueue class which implements a queue using two stacks.
class MyQueue:

    def __init__(self):
        self.stackNewest = []
        self.stackOldest = []

    def enqueue(self, item):
        self.stackNewest.append(item)

    def dequeue(self):
        if self.stackOldest == []:
            while not self.is_stackNewest_Empty():
                popped_data = self.stackNewest.pop()
                self.stackOldest.append(popped_data)
            self.stackOldest.pop()
        else:
            self.stackOldest.pop()

    def is_stackNewest_Empty(self):
        return self.stackNewest == []

    def is_stackOldest_Empty(self):
        return self.stackOldest == []

    def __str__(self):
        return str([self.stackNewest, self.stackOldest])
        if self.is_stackOldest_Empty:
            return str(self.stackNewest)
        elif self.is_stackNewest_Empty and self.is_stackOldest_Empty:
            return str(self.stackNewest, self.stackOldest)
        else:
            return str(self.is_stackNewest_Empty)



x = MyQueue()
x.enqueue(1)
x.enqueue(2)
x.enqueue(3)
x.enqueue(4)
x.enqueue(5)
x.enqueue(6)
x.enqueue(7)
x.enqueue(8)
x.enqueue(9)
x.enqueue(10)

print(x)
x.dequeue()
print(x)
x.dequeue()
print(x)
x.dequeue()
print(x)
x.dequeue()

print(x)
