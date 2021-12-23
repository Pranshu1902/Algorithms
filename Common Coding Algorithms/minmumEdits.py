# if we are given two string str1 and str2 then how many minimum number of operations can be performed on the str1 that it gets converted to str2.The Operations can be:
#1. Insert
#2. Remove
#3. Replace

def minEdits(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for x in range(m + 1)] for x in range(n + 1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j] = i
            elif s1[i-1]==s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
#                                   remove      insert     replace
    print(dp[n][m])


minEdits("saturday", "sunday")

