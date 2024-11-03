class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = {}

        #build the graph
        for (a, b), value in zip(equations, values):
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}
            #edge, path 
            graph[a][b] = value
            graph[b][a] = 1 / value

        #once we have the graph now we can implement dfs
        def dfs(start, end, visited, curr_prod):
            if start == end:
                return curr_prod
            
            visited.add(start)
            for (neighbor, weight) in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited, curr_prod*weight)
                    if result != -1:
                        return result
            
            visited.remove(start)
            return -1
        

        #answer each query
        results = []

        for c,d in queries:
            if c not in graph or d not in graph:
                results.append(-1.0)

            else:
                result = dfs(c, d, set(), 1.0)
                results.append(result)

        return results

            









        