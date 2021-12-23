def checkAnangram(s1, s2):
    if len(s1)!=len(s2):
        return False
    d1={}
    for i in s1:
        if i in d1.keys():
            d1[i]+=1
        else:
            d1[i]=1
    for i in s2:
        if d1[i]>=1:
            d1[i]-=1
        else:
            return False
    final = d1.values()
    if len(set(final))==1:
        return True
    return False

print(checkAnangram("stackoverflow", "flowerovstack"))
