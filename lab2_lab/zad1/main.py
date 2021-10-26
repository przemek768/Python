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
            n = Node(value)
            self.head = n
            self.tail = n
        else:
            n = Node(value)
            n.next = self.head
            self.head = n

    def append(self, value: Any) -> None:
        if self.head != None:
            n = self.tail
            n.next = Node(value)
            self.tail = n.next
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
            n = self.tail
        if len(self) > at:
            n = self.head
            for x in range(at):
                n = n.next
        return n

    def insert(self, value: Any, after: Node) -> None:
        if after == self.tail:
            self.append(value)
            return
        if after == None:
            return False
        n = Node(value)
        n.next = after.next
        after.next = n

    def pop(self) -> Any:
        if self.head != None:
            n = self.head
            self.head = n.next
            return n.value
        else:
            return False

    def remove_last(self) -> Any:
        n = self.head
        if self.head == None:
            return False
        if len(self) == 1:
            delete = self.head
            self.head = None
            return delete.value
        if len(self) == 2:
            delete = self.tail
            self.tail = self.head
            self.head.next = None
            return delete.value
        if len(self) > 2:
            n = self.node(len(self)-3)
            self.tail = n
            n = n.next
            delete = n.next
            n.next = None
            return delete.value

    def remove(self, after: Node) -> Any:
        n = self.head
        if len(self) == 1:
           return False
        if after.next == self.tail:
            delete = self.tail
            self.remove_last()
        else:
            while n.next != after:
                n=n.next
            delete = n.next
            n.next = after.next
        return delete.value

    def __len__(self):
        n = self.head
        count = 0
        while n != None:
            count += 1
            n = n.next
        return count

    def __str__(self):
        display = ""
        n = self.head
        for x in range(len(self)):
            if n.next != None:
                display+=str(n.value)+"->"
            if n.next == None:
                display+=str(n.value)
            n = n.next
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
        self.storage = LinkedList()

    def peek(self) -> Any:
        if len(self.storage) != 0:
            return self.storage.tail.value
        else:
            return False

    def enqueue(self, element: Any) -> None:
        self.storage.push(element)

    def dequeue(self) -> Any:
        if len(self.storage) != 0:
            return self.storage.remove_last()
        else:
            return False

    def __len__(self):
        return len(self.storage)

    def __str__(self):
        display = ""
        for x in range(len(self.storage)):
            display += str(self.storage.node(x).value)+" "
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
