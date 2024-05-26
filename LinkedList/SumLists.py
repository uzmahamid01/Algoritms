class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sumLists(data_list1, data_list2):
    # you have two numbers represented by a linked list, 
    #input: (7->1->6) + (5->9->2) = 617 + 295 = 912
    #output: 2->1->9
    # you have to add them together and return the sum as a linked list
    # you are allowed to convert the input to integers
    if data_list1 is None or data_list2 is None:
        return None
    if data_list1.next is None and data_list2.next is None:
        return Node(data_list1.data + data_list2.data)
    else:
        sum = data_list1.data + data_list2.data
        if sum >= 10:
            sum = sum % 10
            data_list1.next = sumLists(data_list1.next, data_list2.next)
        else:
            data_list1.next = sumLists(data_list1.next, data_list2.next)
        return Node(sum)
    
    
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
