class Node:
    # Function to initialze the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as None


# Linked List class contains a Node object
class LinkedList:
    # Function to initialize head
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

    # Print the linked list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == "__main__":
    llist = LinkedList()

    llist.iEnd(6)  # 6->None
    llist.iStart(7)  # 7->6->None
    llist.iStart(1)  # 1->7->6->None
    llist.iEnd(4)  # 1->7->6->4->None
    llist.iAfter(llist.head.next, 8)  # 1 -> 7-> 8-> 6-> 4-> None

    print("Linked list is:", end="")
    llist.printList()
