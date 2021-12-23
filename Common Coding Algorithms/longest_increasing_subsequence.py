def lis(a, n):
    lis = []
    parent = []

    for i in range(n):
        lis.append(1)
    for i in range(n):
        parent.append(-1)

    for i in range(n):
        for j in range(i):

            if a[j] < a[i]:
                if lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
                    parent[i] = j

    length = 0
    pos = 0

    for i in range(n):
        if length < lis[i]:
            length = lis[i]
            pos = i

    print("Length:", length)
    sequence = []

    while pos != -1:
        sequence.append(a[pos])
        pos = parent[pos]

    sequence.reverse()

    for i in range(length):
        print(sequence[i], end=" ")


a = [2, 5, 3, 7, 11, 8, 10, 13, 6]
n = len(a)

lis(a, n)
