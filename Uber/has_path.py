from collections import deque
class Solution(object):
    #dfs
    def hasPath(self, graph, src, dst):
        if src == dst:
            return True
        
        for neighbor in graph[src]:
            if self.hasPath(graph, neighbor, dst):
                return True
            
        return False
    

    #bfs: no recursion possible here 
    def hasPath(self, graph, src, dst):
        queue = deque([src])
        
        while queue:
            curr_node = queue.popleft()
            
            if curr_node == dst:
                return True
            
            for neighbor in graph[curr_node]:
                queue.append(neighbor)
                
        return False