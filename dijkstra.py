# input graph

#         4
#     C-------D
#  3/ | \1      \ 1
# A  2|  E--------B
# \   | /3   2   / 2
#  \2 |/       /
#     F-------G
#         5


graph = {
    "A":{("C",3),("F",2)},
    "C":{("A",3),("F",2),("E",1),("D",4)},
    "F":{("A",2),("C",2),("E",3),("B",6),("G",5)},
    "E":{("C",1),("F",3),("B",2)},
    "D":{("C",4),("B",1)},
    "G":{("F",5),("B",2)}
}


def dijkstra(graph, start, end, all_nodes):
    pointer=[]
    current=start

    # creating the net distance dictionary
    inf = float('inf')
    dist={}
    for i in all_nodes:
        if i==start:
            dist[i]=0
        else:
            dist[i]=inf

    move=0
    while current!=end:
        # updating the search
        move+=1

        # available vertexes to go from current vertex
        options = graph[current]
        for val, d in options:
            # distance to reach current vertex
            previous = dist[current]
            new = previous + d
            # updating the distance to the new vertex if is smaller
            if new<dist[val]:
                # removing previous longer paths
                for i,j in pointer:
                    if j==val:
                        pointer.remove([i,j])
                # adding the new shorter path
                pointer.append([current, val])
                dist[val]=new

        # updating current to the closest vertex
        others = list(dist.values())
        others.sort()
        next = others[move]
        keys = [k for k, v in dist.items() if v == next]
        keys=keys[0]

        current = keys

    # printing the path
    print("Solution path")
    node = end
    path=[end]
    while node!=start:
        for star, to in pointer:
            if to==node:
                path.append(star)
                node = star
    print(path[::-1])
    print()
    print("Graph with updated distances")
    print(dist)
    print()
    print("Distance to reach {} from {}".format(end, start))
    print(dist[end])

nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

dijkstra(graph, "A", "B", nodes)
