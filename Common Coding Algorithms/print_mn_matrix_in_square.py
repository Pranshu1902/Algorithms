def loops(m,n):
    a=min(m,n)
    if a%2==0:
        return a//2
    return (a+1)//2
def getSquare(m,n):
    num = loops(m,n)
    for i in range(num):
        for j in range(i,m-1-i):
            print(i+" "+j)
        for k in range(1,n-1-i):
            print(k+" "+j)
        for l in range(j,i,-1):
            print(k+" "+l)
        for x in range(k,i,-1):
            print(x+" "+l)

