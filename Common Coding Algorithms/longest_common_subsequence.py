def lcs(s1, s2):
    table = [[0 for i in range(len(s1)+1)]for j in range(len(s2)+1)]
    for i in range(len(s2)+1):
        for j in range(len(s1)+1):
            if i==0 or j==0:
                table[i][j]=0
            elif s1[j-1]==s2[i-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i][j-1], table[i-1][j])

    print(table[len(s2)][len(s1)])
    return table, table[len(s2)][len(s1)]

#lcs("abcdaf", "acbcf")

def getLCS(s1, s2):
    table, temp = lcs(s1, s2)
    s = []
    i = len(s2)
    j = len(s1)
    while i != 0 and j != 0:
        if s1[j-1]==s2[i-1] and table[i-1][j-1] == table[i][j] - 1:
            s.append(s1[j-1])
            i-=1
            j-=1
        elif table[i-1][j]==table[i][j]:
            i-=1
        else:
            j-=1
    print("".join(s[::-1]))

getLCS("abcdaf", "acbcf")
