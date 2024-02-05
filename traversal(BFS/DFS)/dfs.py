#going down the tree
#         9
#     4       20
#  1   6    15      170

#Inorder = [1,  4, 6, 9, 15, 20, 170] LSR
#PreOrder = [9, 4, 1, 6, 20, 15, 170] SLR
#PostOrder = [1, 6, 4,  15, 170, 20, 9] LRS

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Dfs():
    def __init__(self):
        self.root=None
        
    def insert(self,val):
        new_node = Node(val)
        if self.root == None:
            self.root = new_node
            return 
        temp = self.root
        while True:
            if new_node.val < temp.val:
                if temp.left == None:
                    temp.left = new_node
                    break
                else:
                    temp = temp.left
            elif new_node.val > temp.val:
                if temp.right == None:
                    temp.right = new_node
                    break
                else:
                    temp = temp.right

    def lookup(self,val):
        temp = self.root
        while temp is not None:
            if temp.val == val:
                return True
            elif temp == None:
                return False
            elif val < temp.val:
                temp = temp.left
            elif val > temp.val:
                temp = temp.right 

    def InorderDfs(self, node, list):
        if node.left:
            self.InorderDfs(node.left,list)
        list.append(node.val)

        if (node.right):
            self.InorderDfs(node.right,list)
        
        return list
        

    def PreorderDfs(self, node, list):
        list.append(node.val)
        if node.left:
            self.PreorderDfs(node.left,list)
        
        if (node.right):
            self.PreorderDfs(node.right,list)
        
        return list
    
    def PostorderDfs(self, node, list):
        
        if node.left:
            self.PostorderDfs(node.left,list)
        
        if (node.right):
            self.PostorderDfs(node.right,list)

        list.append(node.val)
        return list

         
    

# Testing the code
tree=Dfs()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
# print(tree.InorderDfs())

print("Inorder DFS: ", tree.InorderDfs(tree.root, []))
print("Preorder DFS: ", tree.PreorderDfs(tree.root, []))
print("Postorder DFS: ", tree.PostorderDfs(tree.root, []))



