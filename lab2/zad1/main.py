from typing import Any




class Node:
    def __init__(self, value:Any):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __len__(self):
        node = self.head
        count = 0
        while node != None:
            count += 1
            node = node.next
        return count

    def __str__(self):
        strng = ""
        node = self.head
        for x in range(len(self)):
            if node.next != None:
                strng+=str(node.value)+" -> "
            if node.next == None:
                strng+=str(node.value)
            node = node.next
        return strng

    def push(self, value: Any):
        if self.head == None:
            node = Node(value)
            self.head = node
            self.tail = node
        else:
            node = Node(value)
            node.next = self.head
            self.head = node

    def append(self, value: Any):
        if self.head != None:
            node = self.tail
            node.next = Node(value)
            self.tail = node.next
        else:
            self.push(value)

    def node(self, at: int):
        if len(self) == 0:
            raise ValueError("pusto")
        if at == len(self)-1:
            node = self.tail
        if len(self) > at:
            node = self.head
            for x in range(at):
                node = node.next
        return node

    def insert(self, value: Any, after: Node):

        if after == self.tail:
            self.append(value)
            return
        if after == None:
            return
        node = Node(value)
        node.next = after.next
        after.next = node

    def pop(self):
        if self.head != None:
            node = self.head
            self.head = node.next
            return node
        else:
            return False

    def remove_last(self):
        node = self.head
        if self.head == None:
            raise ValueError("pusto")
        if len(self) == 1:
            deleted = self.head
            self.head = None
            return deleted
        if len(self) == 2:
            deleted = self.tail
            self.tail = self.head
            self.head.next = None
            return deleted
        if len(self) > 2:
            node = self.node(len(self)-3)
            self.tail = node
            node = node.next
            deleted = node.next
            node.next = None
            return deleted

    def remove(self, after: Node):
        node = self.head
        if len(self) == 1:
           raise ValueError("jest tylko 1 element")
        if after.next == self.tail:
            deleted = self.tail
            self.remove_last()
        else:
            while node.next != after:
                node=node.next
            deleted = node.next
            node.next = after.next

        return deleted

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
