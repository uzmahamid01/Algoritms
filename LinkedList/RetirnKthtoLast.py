class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#using iterative approach
def findKthToLast(head, k):
    if k < 1 or head is None:
        return None

    pntr1 = head
    pntr2 = head

    # Advance pntr2 by n-1 nodes
    for i in range(k - 1):
        if pntr2 is None:
            # This is an error condition to check to see if
            # the linked list is less than n nodes long, in which
            # case we just return None indicating an error
            return None
        else:
            pntr2 = pntr2.next
    
    # Check if pntr2 became None after the loop, which means n is greater than the length of the list
    if pntr2 is None:
        return None

    # Now, keep going until you hit a null node,
    # and then you've reached the end, and
    # pntr1 will be pointing to the nth from
    # last node
    while pntr2.next is not None:
        pntr1 = pntr1.next
        pntr2 = pntr2.next

    return pntr1


#using recursive approach
def findKthToLast2(head, k):
    if head is None:
        return None, 0
    node, index = findKthToLast2(head.next, k)
    index += 1
    if index == k:
        return head, index
    return node, index


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

head = createLinkedList([1, 2, 3, 4, 5, 6])
n = 5
result = findKthToLast(head, n)
if result:
    print(f"The {n}th to last node is {result.data}")
else:
    print("The list is shorter than n nodes.")

n = 4
result, _ = findKthToLast2(head, n)
if result:
    print(f"The {n}th to last node is {result.data}")
else:
    print("The list is shorter than n nodes.")
