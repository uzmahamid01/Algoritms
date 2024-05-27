class StackNode():
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None
    
    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
        print(data + " pushed to stack ")
        return self.root
            
        
    def pop(self):
        if self.isEmpty():
            print ("Stack is empty")
        temp = self.root
        self.root = self.root.next
        return temp.data
    
    def peek(self):
        if self.isEmpty():
            print ("Stack is empty")
        return self.root.data

# Test the MyStack class
stack = MyStack()
stack.push(str(10))
stack.push(str(20))
stack.push(str(30))
popped_element = stack.pop()
if popped_element is not None:
    print(popped_element + " popped from stack")  # Expected output: "30 popped from stack"
else:
    print("Nothing to pop, stack was empty")

top_element = stack.peek()
if top_element is not None:
    print("Top element in the stack: " + top_element)
else:
    print("Stack is empty, no top element")

# Trying to print elements present in stack array is incorrect, since we don't have an array.
# Instead, we can traverse the stack and print its elements.
print("Elements present in stack:")
current = stack.root
while current is not None:
    print(current.data)
    current = current.next


