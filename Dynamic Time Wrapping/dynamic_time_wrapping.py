def dtw(sample ,test):
    n = len(sample)
    m = len(test)
    inf = float('inf')
    table = [[0 for i in range(m+1)]for i in range(n+1)]
    for i in range(n+1):
        table[i][0] = inf
    for i in range(m+1):
        table[0][i] = inf
    table[0][0] = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            table[i][j] = abs(sample[i-1] - test[j-1]) + min(table[i-1][j-1], table[i][j-1], table[i-1][j])
    
    print(table[n][m])

t = [1,1,2,2,3,5]
s = [1,2,3,5,5,5,6]
dtw(s, t)
