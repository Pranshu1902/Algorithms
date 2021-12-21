inf = float('inf')
dist = [[0,3,6,15],
        [inf,0,-2,inf],
        [inf,inf,0,2],
        [1,inf,inf,0]]

N = None

path = [[N,1,1,1],
        [N,N,2,N],
        [N,N,N,3],
        [4,N,N,N]]

def floyd_warshall(dist, path, source, destination):
    n = len(dist)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]

    # printing the result
    s = [destination]

    while path[source][destination] != source:
        s.append(path[source][destination])
        destination = path[source][destination]

    print(source)
    while len(s)!=0:
        print(s.pop())
