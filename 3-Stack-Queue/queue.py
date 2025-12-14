# Function List: enqueue | dequeue | front | rear | empty | size


class Queue:
    # FIFO queue implementation using a Python list as underlying storage.
    # moderate capacity for all new queues

    DEFAULT_CAPACITY = 10

    def __init__(self):
        # Create an empty queue.
        self._data = [None] * Queue.DEFAULT_CAPACITY
        self._length = 0
        self._frontIndex = 0

    def size(self):
        # Return the number of elements in the queue.
        return self._length

    def empty(self):
        # Return True if the queue is empty.
        return self._length == 0

    def front(self):
        # Return (but do not remove) the element at the front of the queue.
        # Raise Empty exception if the queue is empty.

        if self.empty():
            print("Queue is empty.")
            pass
        return self._data[self._frontIndex]

    def rear(self):
        # Return (but do not remove) the element at the end of the queue.
        # Raise Empty exception if the queue is empty.

        if self.empty():
            print("Queue is empty.")
            return
        index = self._frontIndex + self._length - 1
        return self._data[index]

    def dequeue(self):
        # Remove and return the ﬁrst element of the queue (i.e., FIFO).
        # Raise Empty exception if the queue is empty.

        if self.empty():
            print("Queue is empty.")
            return

        answer = self._data[self._frontIndex]
        self._data[self._frontIndex] = None  # help garbage collection
        self._frontIndex = (self._frontIndex + 1) % len(self._data)
        self._length -= 1

        #      if 0 < self.size < len(self.data) // 4:
        #         self._resize(len(self.data) // 2)

        return answer

    def enqueue(self, e):
        # Add an element to the back of queue.
        if self._length == len(self._data):
            # double the array size
            self._resize(2 * len(self.data))
        avail = (self._frontIndex + self._length) % len(self._data)
        self._data[avail] = e
        self._length += 1

    def _resize(self, cap):  # we assume cap >= len(self)
        # Resize to a new list of capacity >= len(self).
        # keep track of existing list
        old = self._data  # allocate list with new capacity
        self._data = [None] * cap
        walk = self._frontIndex

        for k in range(self._length):  # only consider existing elements
            self._data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus

        self._frontIndex = 0  # front has been realigned


Q = Queue()
Q.enqueue(5)  # 5
Q.enqueue(3)  # 5 <- 3
print(Q.size())  # returns 2
print(Q.dequeue())  # returns 5
print(Q.empty())  # false
print(Q.dequeue())  # returns 3
Q.empty()  # true
Q.dequeue()  # Queue is empty.
Q.enqueue(7)  # 7
Q.enqueue(9)  # 7 <- 9
print(Q.front())  # 7
Q.enqueue(4)  # 7 <- 9 <- 4
print(Q.rear())  # 4
print(Q.size())  # 3
print(Q.dequeue())  # 9 <- 4 | returns 7
