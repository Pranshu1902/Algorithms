graph = {1:[[3,2],[4,4]], 2:[[3,10]], 3:[[4,-1]], 4:[[5,7], [6,5]], 5:None, 6:None}


def bellman_ford(graph, n, source):
    d={}
    inf = float('inf')
    parent = {}
    for i in range(1,n+1):
        d[i]=inf
        parent[i] = None

    d[source] = 0
    while True:
        for i in range(1,n+1):
            flag = False
            start = i
            if graph[start]!=None:
                for point, cost in graph[start]:
                    if d[start] + cost < d[point]:
                        d[point] = d[start] + cost
                        parent[point] = start
                        flag = True
        if flag==False:
            break

    # Detecting negative cycle
    for i in range(1,n+1):
        start = i
        if graph[start]!=None:
            for point, cost in graph[start]:
                if d[start] + cost < d[point]:
                    print("Negative Cycle present")
                    break

    # printing the results

    print("Distance:")
    print(d)
    print("Parent:")
    print(parent)

bellman_ford(graph, 6, 1)
