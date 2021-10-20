from typing import Any
import int
class  Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def show_list(self):
        if self.head is None:
            print("Lista jest pusta")
            return
        else:
            n = self.head
            while n is not None:
                print(n.value, " ")
                n = n.next
    
    def push_at_first(self, value: Any):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append_at_end(self, value: Any):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
    def insert(self, value: Any, after: None):
        n = self.head
        while n is not None:
            if after==n.value:
                break
            n = n.next
        if n is None:
            print("Brak w liscie")
        else:
            new_node = Node(value)
            new_node.next = n.next
            n.next = new_node
    def pop(self):
        node = self.head
        self.head = node.next
        return node
    def remove_last(self):
        if self.head is None:
            print("Pusto")
        elif self.head is None:
            self.head = None
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None
    def remove(self, after: None):
        if after is not None:
            if after.next == None:
                return
        if after is None:
            return
        n = self.head
        while node is not after:
            n = n.next
        n = n.next
        after.next = n.next

    def length(self):
        n = self.head
        ct = 0
        while n is not None:
            ct += 1
            n = n.next
        return ct

    def node(self, at: int):
        if self.length() >= at:
            n = self.head
            for x in range(at):
                n = n.next
            return n

lista = LinkedList()
node=Node(2)
print(node)
lista.push_at_first(5)
lista.push_at_first(6)
lista.push_at_first(7)
lista.push_at_first(8)
lista.append_at_end(100)
lista.push_at_first(20)
lista.insert(30, 5)
lista.pop()
lista.remove_last()
lista.remove(lista.node(2))
lista.show_list()
