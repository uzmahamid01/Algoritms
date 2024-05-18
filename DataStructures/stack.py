class Stack(object):
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []
    
    def push(self,item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]   #top most item
    
    def size(self):
        return len(self.stack)
    
s = Stack()

s.push(2)
s.push(3)
s.push(4)
s.push(5)

print(s.stack)

print(s.size())

s.pop()

print(s.stack)

print(s.peek())




