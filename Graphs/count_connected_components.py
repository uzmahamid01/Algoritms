def countComponents(n, edges):
    par = [i for i in range(n)]

    rank = [1]*n

    def find(n1):
        res = n1

        while res != par[res]:
            par[res] = par[par[res]]
            res = par[res]
        return res

    def union(n1,n2):
        #find the root parent for each node
        p1 = find(n1)
        p2 = find(n2)

        if n1 == n2:
            return 0

        if rank[p2]> rank[p1]:
            par[p1] = p2
            rank[p2] += rank[p1]
        else:
            par[p2] = p1
            rank[p1] += rank[p2]

        return 1

    res = n
    for n1, n2 in edges:
        res -= union(n1, n2)
    return res



def main():
    graph = [[0,1],[0,2],[0,3],[4,5]]
    print(countComponents(6, graph))
    
main()
