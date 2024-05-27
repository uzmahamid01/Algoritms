class MyStack():
    def __init__(self):
        self.stack = []
        self.size = 0

    def createStack(self):
        self.stack = []
        self.size = 0
        return self.stack
    
    def push(self, item):
        self.stack.append(item)
        self.size += 1
        print(item + " pushed to stack ")
        return self.stack
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            self.size -= 1
            return self.stack.pop()
    
    def isEmpty(self):
        return self.size == 0
            
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.stack[-1]

# Testing the MyStack class
stack = MyStack()
stack.push(str(10))
stack.push(str(20))
stack.push(str(30))
print(stack.pop() + " popped from stack")  # Expected output: "30 popped from stack"
print("Top element in the stack array " + stack.peek())
print("Elements present in stack" + str(stack.stack))

