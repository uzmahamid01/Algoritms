class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None  # New attribute to store the reference to the previous node
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None  # New attribute to store the tail node
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for i in range(index):
            curr = curr.next
        
        return curr.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = Node(val)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = Node(val)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            curr = self.head
            for i in range(index-1):
                curr = curr.next
            node = Node(val)
            node.next = curr.next
            curr.next.prev = node
            curr.next = node
            node.prev = curr

            self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return

        if self.size == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            curr = self.head
            for i in range(index):
                curr = curr.next
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

        self.size -= 1
