Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buﬀer is not allowed?





#with buffer with O(N) space and time complexity

class Node:

    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = Node()

    def append(self, data):
        newNode = Node(data)
        cur = self.head

        while cur.next:
            cur = cur.next
        cur.next = newNode

    def display(self):
        show = []
        cur = self.head

        while cur.next:
            cur = cur.next
            show.append(cur.data)
        return show

    def __str__(self):
        show = self.display()
        return(str(show))

  #with buffer with O(N) space and time complexity
    def unique2(self):
        cur = self.head  # set the current node we are looking at the head node
        dic = {}         # creating an hashtable to store the occurence of each element in the LinkedList
        prev = None

        while cur.next:
            if cur.data in dic:
                prev.next = cur.next
            else:
                dic[cur.data] = 1
                prev = cur
            cur = cur.next

        return

 

#without a buffer using a forerunner space complexity is O(1) and Time complexity is O(N2)
    def unique2(self):
        current  = self.head.next   #since head in my design is None we set current to the next value

        while current != None:
            runner = current    # create the runner, which goes ahead to check if our current value has a duplicate
            while runner.next != None:
                if runner.next.data == current.data:   #If it does make delete value from the list
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
            
     
list = LinkedList()

list.append(1)
list.append(2)
list.append(3)
list.append(1)
list.append(4)
list.append(12)

list.unique2()
print(list)
