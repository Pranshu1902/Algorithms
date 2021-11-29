# Change Making Problem

# Number of ways to making 5 using coins of 1 and 2

target = 5

coins = [1,2]

ways = [1]+[0]*target

for c in coins:
    for i in range(c,target+1):
        ways[i]+=ways[i-c]
print(ways[target])

