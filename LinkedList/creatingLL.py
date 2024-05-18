class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def appendToTail(self, data):
        end = Node(data)
        n = self
        while n.next:
            n = n.next
        n.next = end

    def appendAfter(self, data, new_data):
        n = self
        while n:
            if n.data == data:
                new_node = Node(new_data)
                new_node.next = n.next
                n.next = new_node
                return
            n = n.next
        print("Node with data", data, "is not present in the linked list")

    def deleteNode(self, head, d):
        if head is None:
            return None
        
        if head.data == d:
            return head.next  # Move head to next node
        
        current = head
        while current.next is not None:
            if current.next.data == d:
                current.next = current.next.next
                return head
            current = current.next

        return head
    

def appendToFront(head, data):
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head

def printLinkedList(node):
    while node:
        print(node.data, end=" -> " if node.next else "")
        node = node.next

head = Node(1)

head.appendToTail(2)
head.appendToTail(3)

print("Before deletion:")
printLinkedList(head)

head = head.deleteNode(head, 2)

print("\nAfter deletion:")
printLinkedList(head)

head = appendToFront(head, 0)

print("\nAfter front insertion:")
printLinkedList(head)

head.appendAfter(0, 4)

print("\nAfter insertion:")
printLinkedList(head)
