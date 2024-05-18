class BinaryTree:
    def  __init__(self, root):
        self.root = root
        self.left = None
        self.right = None
    
    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)

        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)

        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def getRoot(self):
        return self.root

    def setRootVal(self, newVal):
        self.root = newVal

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right
    

# Create an instance of BinaryTree
r = BinaryTree(3)

# Call methods on the instance
r.insertLeft(4)
r.insertLeft(5)
r.insertRight(6)
r.insertRight(7)

# Access the left child
l = r.getRightChild()
print(l.getRoot())  # Output: 5

# Set the root value of the left child
l.setRootVal(9)
print(r.getRoot())  # Output: 3