class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def partition(head, p):
    if head is None:
        return None
    left_head = None
    left_tail = None
    right_head = None
    right_tail = None

    curr = head
    while curr:
        next_node = curr.next  
        curr.next = None
        if curr.data < p:
            if left_head is None:
                left_head = curr
                left_tail = curr
            else:
                left_tail.next = curr
                left_tail = curr
        else:
            if right_head is None:
                right_head = curr
                right_tail = curr
            else:
                right_tail.next = curr
                right_tail = curr
        curr = next_node

    if left_tail:
        left_tail.next = right_head
        return left_head
    else:
        return right_head
    
def createLinkedList(data_list):
    if not data_list:
        return None
    head = Node(data_list[0])
    current = head
    for data in data_list[1:]:
        current.next = Node(data)
        current = current.next
    return head

def printLinkedList(node):
    while node:
        print(node.data, end=" -> " if node.next else "")
        node = node.next
    print()

head = createLinkedList([3, 5, 8, 5, 10, 2, 1])
print("Original linked list:")
printLinkedList(head)

head = partition(head, 5)

print("\nLinked list after partitioning around 5:")
printLinkedList(head)
