# Function List: push | pop | top | empty | size
# LIFO Stack implementation using a Python list as underlying storage.


class Stack:
    def __init__(self):
        # Create an empty stack.
        self._data = []  # nonpublic list instance

    def size(self):
        # Return the number of elements in the stack.
        return len(self._data)

    def empty(self):
        # Return True if the stack is empty.
        return len(self._data) == 0

    def push(self, e):
        # Add element e to the top of the stack.
        self._data.append(e)  # new item stored at end of list

    def top(self):
        # Return (but do not remove) the element at the top of the stack.
        # Raise Empty exception if the stack is empty.
        if self.empty():
            print("Stack is empty.")
            return

        return self._data[-1]  # the last item in the list

    def pop(self):
        # Remove and return the element from the top of the stack (i.e., LIFO).
        # Raise Empty exception if the stack is empty.
        if self.empty():
            print("Stack is empty")
            return

        return self._data.pop()  # remove last item from list


# Initialize a stack
S = Stack()
S.push(5)
S.push(3)
print(S.size())
print(S.pop())
print(S.empty())
print(S.pop())
print(S.empty())
S.push(7)
S.push(9)
print(S.top())
S.push(4)
print(S.size())
print(S.pop())
S.push(6)
