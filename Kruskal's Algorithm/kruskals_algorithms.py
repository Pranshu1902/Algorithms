# Kruskal's Algorithm

class algo:
    def __init__(self, vertex):
        self.v = vertex
        self.graph = []

    def add(self, x,y,d):
        self.graph.append([x,y,d])

    def find(self, parent, node):
        if parent[node]==node:
            return node
        return self.find(parent, parent[node])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        self.graph = sorted(self.graph, key = lambda x : x[2])
        
        index = 0
        edges = 0

        parent = []
        rank = []
        for x in range(self.v):
            parent.append(x)
            rank.append(0)

        while index<self.v:
            i,j,d = self.graph[index]
            index += 1
            x = self.find(parent, i)
            y = self.find(parent, j)
            if x!=y:# cycle is not created
                edges += 1
                result.append([i,j,d])
                self.union(parent, rank, x, y)

        print(parent)
        print(rank)
        total = 0
        for i in result:
            print("{} => {}, weight = {}".format(i[0],i[1],i[2]))
            total += i[2]
        print("Minimum Spanning Tree =",total)
        print("Number of Edges =",edges)

a = algo(9)
a.add(1,2,1)
a.add(1,3,3)
a.add(2,6,4)
a.add(3,6,2)
a.add(3,4,1)
a.add(4,5,5)
a.add(6,7,2)
a.add(6,5,6)
a.add(7,5,7)

a.kruskal()
