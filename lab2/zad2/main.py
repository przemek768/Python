from typing import Any
class Stack:
    def __init__(self, element):
        self.next = None
        self.element = element

class LinkedStack:
    def __init__(self):
        self.head = None

    def empty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, element: Any) -> None:
        if self.head is None:
            self.head = Stack(element)
        else:
            new_stack = Stack(element)
            new_stack.next = self.head
            self.head = new_stack

    def pop(self) -> Any:
        new_stack = self.head
        self.head = self.head.next
        new_stack.next = None
        return new_stack.element

    def print(self):
        new_stack = self.head
        while new_stack is not None:
            print(new_stack.element)
            new_stack = new_stack.next
        return

    def len(self):
        ct = 0
        new_stack = self.head
        while new_stack is not None:
            new_stack = new_stack.next
            ct += 1
        return ct

stack = LinkedStack()
print(stack.empty())
stack.push(88)
stack.push(55)
stack.push(66)
stack.push(77)
print(stack.pop())
stack.print()
print(stack.len())

