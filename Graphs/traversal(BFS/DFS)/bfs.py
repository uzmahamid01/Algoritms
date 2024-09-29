class Node():
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

class Bfs():
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

    def breadthFirstSearch(self):
        curr_node = self.root
        list = []
        queue = []
        queue.append(curr_node)
        while  len(queue) > 0 :
            curr_node = queue[0]
            del queue[0]
            list.append(curr_node.val)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)

        return  list
    
    def bfsRecursive(self, queue, list):
        if len(queue) == 0:
            return list
        curr_node = queue[0]
        del queue[0]
        list.append(curr_node.val)
        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)
    
        return self.bfsRecursive(queue, list)

      
tree=Bfs()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(7)
print(tree.breadthFirstSearch())

print(tree.bfsRecursive([tree.root], []))
