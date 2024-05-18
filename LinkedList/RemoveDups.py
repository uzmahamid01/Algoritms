#remove duplicates from an unsorted linked list, temporary buffer is not allowed
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeDuplicates(head):
    if head is None:
        return head
    curr = head
    while curr.next is not None:
        runner = curr
        while runner.next is not None:
            if runner.data == runner.next.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr = curr.next
    return head
    
def printLinkedList(node):
    while node:
        print(node.data, end=" -> " if node.next else "")
        node = node.next


    

def main():
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(3)
    head.next.next.next.next.next = Node(4)
    head.next.next.next.next.next.next = Node(5)

    print("Original linked list:")
    printLinkedList(head)
    print("\nLinked list after removing duplicates:")
    removeDuplicates(head)
    printLinkedList(head)


main()
