# Create & Traverse a LinkedList
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

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
