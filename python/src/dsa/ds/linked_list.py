# Create & Traverse a LinkedList
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def iStart(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Inserts a new node after the given prev_node.
    def iAfter(self, prev_node, new_data):
        # Check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must be in LinkedList.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Appends a new node at the end.
    def iEnd(self, new_data):
        new_node = Node(new_data)
        # If the Linked List is empty, then make the new node as head
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Delete the first occurrence of the given data
    def deleteNode(self, key):
        temp = self.head
        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return
        prev.next = temp.next
        temp = None

    # Delete a node at the given position
    def deleteNodeAt(self, position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return self.head
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == position:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = temp
        return prev

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)

    second = Node(2)
    llist.head.next = second

    third = Node(3)
    second.next = third

    llist.printList()

