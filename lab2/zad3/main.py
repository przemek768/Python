from typing import Any
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    def get_data(self):
        return self.value
    def get_next(self):
        return self.next
    def set_next(self, new_node):
        self.next = new_node

class Queue:
    def __init__(self, head=None):
        self.head = head

    def enqueue(self, value: Any):
        new_element = Node(value)
        n = self.head
        if n is None:
            self.head = new_element
        else:
            while n.get_next():
                n = n.get_next()
            n.set_next(new_element)

    def dequeue(self):
        n = self.head
        if n != None:
            self.head = n.get_next()
            return n.value
        else:
            print("Pusto")

    def __len__(self):
        return len(self.temp)

    def peek(self):
        return self.head

    def print(self):
        n= self.head
        self.temp = []
        while n:
            self.temp.append(n.get_data())
            n = n.get_next()
        print(self.temp)

q = Queue()
print(q.peek())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.dequeue())
q.print()
print(len(q))
