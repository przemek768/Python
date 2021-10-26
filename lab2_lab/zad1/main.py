from typing import Any
class Node:
    def __init__(self, value:Any):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value: Any) -> None:
        if self.head == None:
            node = Node(value)
            self.head = node
            self.tail = node
        else:
            node = Node(value)
            node.next = self.head
            self.head = node

    def append(self, value: Any) -> None:
        if self.head != None:
            node = self.tail
            node.next = Node(value)
            self.tail = node.next
        else:
            self.push(value)

    def node(self, at: int) -> Node:
        if len(self) == 0:
            return False
        if at < 0:
            return False
        if at > len(self)-1:
            return False
        if at == len(self)-1:
            node = self.tail
        if len(self) > at:
            node = self.head
            for x in range(at):
                node = node.next
        return node

    def insert(self, value: Any, after: Node) -> None:
        if after == self.tail:
            self.append(value)
            return
        if after == None:
            return False
        node = Node(value)
        node.next = after.next
        after.next = node

    def pop(self) -> Any:
        if self.head != None:
            node = self.head
            self.head = node.next
            return node.value
        else:
            return False

    def remove_last(self) -> Any:
        node = self.head
        if self.head == None:
            return False
        if len(self) == 1:
            deleted = self.head
            self.head = None
            return deleted.value
        if len(self) == 2:
            deleted = self.tail
            self.tail = self.head
            self.head.next = None
            return deleted.value
        if len(self) > 2:
            node = self.node(len(self)-3)
            self.tail = node
            node = node.next
            deleted = node.next
            node.next = None
            return deleted.value

    def remove(self, after: Node) -> Any:
        node = self.head
        if len(self) == 1:
           return False
        if after.next == self.tail:
            deleted = self.tail
            self.remove_last()
        else:
            while node.next != after:
                node=node.next
            deleted = node.next
            node.next = after.next
        return deleted.value

    def __len__(self):
        node = self.head
        count = 0
        while node != None:
            count += 1
            node = node.next
        return count

    def __str__(self):
        display = ""
        node = self.head
        for x in range(len(self)):
            if node.next != None:
                display+=str(node.value)+"->"
            if node.next == None:
                display+=str(node.value)
            node = node.next
        return display

#zad1
print("Zad1")
lista = LinkedList()
lista.push(5)
lista.push(6)
lista.push(7)
lista.push(8)
lista.append(9)
print(lista.node(2))
lista.insert(2,lista.node(3))
print(lista.pop())
print(lista.remove_last())
lista.remove(lista.node(2))
print(str(lista))
print(len(lista))

class Stack:
    def __init__(self):
       self.storage = LinkedList()

    def push(self, element:Any) -> None:
        self.storage.push(element)

    def pop(self) -> Any:
        if len(self.storage) != 0:
            return self.storage.pop()
        else:
            return False

    def __len__(self):
        return len(self.storage)

    def __str__(self):
        display = ""
        for x in range(len(self.storage)):
            display+=str(self.storage.node(x).value)+"\n"
        return display

#zad2
print("\n"+"Zad2")
stack = Stack()
assert len(stack) == 0
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
print(stack.pop())
print(str(stack))
print(len(stack))

class Queue:
    def __init__(self):
        self._storage = LinkedList()

    def peek(self) -> Any:
        if len(self._storage) != 0:
            return self._storage.tail.value
        else:
            return False

    def enqueue(self, element: Any) -> None:
        self._storage.push(element)

    def dequeue(self) -> Any:
        if len(self._storage) != 0:
            return self._storage.remove_last()
        else:
            return False

    def __len__(self):
        return len(self._storage)

    def __str__(self):
        display = ""
        for x in range(len(self._storage)):
            display += str(self._storage.node(x).value)+" "
        return display

#zad3
print("\n"+"Zad3")
queue = Queue()
assert len(queue) == 0
print(queue.peek())
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
print(queue.peek())
print(queue.dequeue())
print(str(queue))
print(len(queue))
