# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop() should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a specifc substack

class Set_Of_stacks:
    def __init__(self, capacity):
        self.stacks = []
        if capacity < 1:
            raise CapacityError("Capacity has to be greater or equal to One")
        else:
            self.capacity = capacity

    def __str__(self):
        return str(self.stacks)

    def push(self, item):
        if self.stacks == [] or len(self.stacks[-1]) >= self.capacity:
            self.stacks.append([item])
        else:
            self.stacks[-1].append(item)

    def pop(self):
        if self.stacks == []:
            raise EmptyError("Can't pop from an empty stacks")
        else:
            popped = self.stacks[-1][-1]
            if len(self.stacks[-1]) == 1:
                del self.stacks[-1]
            else:
                self.stacks[-1].pop()
        return popped

    def popAt(self, index):
        if self.stacks == [] or index > len(self.stacks):
            raise IndexError("Can't pop an empty stack")
        else:
            popped = self.stacks[index][-1]
            print(str(popped))
            if len(self.stacks[index]) == 1:
                del self.stacks[-1]
            elif len(self.stacks) == index:
                del self.stack[-1][-1]
            else:
                if index == len(self.stacks)-1:
                    self.stacks[-1].pop
                else:
                    self.stacks[index][-1] = self.stacks[index+1][0]
                for i in range(index+1, len(self.stacks)):
                    for j in range(0, len(self.stacks[i])):
                        if j == len(self.stacks[i]) - 1 and i != (len(self.stacks)-1):
                            self.stacks[i][j] = self.stacks[i+1][0]
                        elif j !=len(self.stacks[i]) - 1 and i != (len(self.stacks)-1):
                            self.stacks[i][j] = self.stacks[i][j+1]
                        elif j !=len(self.stacks[i]) - 1 and i == (len(self.stacks)-1):
                            self.stacks[i][j] = self.stacks[i][j+1]

                del self.stacks[-1][-1]
                if len(self.stacks[-1]) == 0:
                    del self.stacks[-1]
        return popped


x = Set_Of_stacks(3)
x.push(1)
x.push(2)
x.push(3)
x.push(4)
x.push(5)
x.push(6)
x.push(7)
x.push(8)

print(x)
x.popAt(1)
print(x)
x.popAt(1)
print(x)
x.popAt(1)
print(x)
x.popAt(1)
print(x)
x.popAt(1)
print(x)
