class Node:
    def __init__(self, data):
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

    # Print the linked list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


llist = LinkedList()
llist.iStart(7)
llist.iStart(1)
llist.iStart(3)
llist.iStart(2)

print("Created Linked List: ")
llist.printList()
llist.deleteNode(1)
print("\nLinked List after Deletion of 1:")
llist.printList()

llist.deleteNodeAt(1)
print("\nLinked List after Deletion at position 1:")
llist.printList()
