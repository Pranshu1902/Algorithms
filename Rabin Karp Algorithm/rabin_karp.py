def rk(text, pattern, prime):
    d = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}

    n=len(pattern)
    num = 0
    for i in range(len(pattern)):
        num += d[pattern[i]]*(prime**i)

    number = 0
    for i in range(n):
        number += d[text[i]]*(prime**i)
    for i in range(len(text) - n):
        sub = text[i:i+n]
        if number==num:
            if sub==pattern:
                print("Match at index",i)
        number -= d[sub[0]]
        number //= prime
        number += d[text[i+n]]*(prime**(n-1))

rk("yeminsajid", "nsa", 11)
