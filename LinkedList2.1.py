Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buﬀer is not allowed?





#with buffer with O(N) space and time complexity
    def removeDuplicate(self):
        unique = {}             # creating an hashtable to store the occurence of each element in the LinkedList
        cur = self.head         # set the current node we are looking at the head node

        while cur.next != None:
            lastnode = cur        #keeping track of previous node
            cur = cur.next
            unique[cur.data] = 1  # assigning 1 to element encountered for the first time

            if unique[cur.data] >= 1:
                unique[cur.data] += 1  # adding 1 to eleement seen before

            if unique[cur.data] > 1:
                lastnode.next = cur.next  # if element is not unique remove element from the list
        return

#without a buffer using a forerunner space complexity is O(1) and Time complexity is O(N2)
    def removeDuplicate2(self):
        current  = self.head.next   #since head in my design is None we set current to the next value

        while current != None:
            runner = current    # create the runner, which goes ahead to check if our current value has a duplicate
            while runner.next != None:
                if runner.next.data == current.data:   #If it does make delete value from the list
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
