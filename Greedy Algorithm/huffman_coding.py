# Huffman code


d = {"a":45, "b":13, "c":12, "d":16, "e":9, "f":5}

val = [45,13,12,16,9,5]
key = ["a","b","c","d","e","f"]

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

pq = []
a = sorted(val)
for i in a:
    pq.append(Node(i))

# Compression
while len(pq)!=1:
    x = pq.pop(0)
    y = pq.pop(0)
    edge = Node(x.data+y.data)
    if x.data<y.data:
        edge.left = x
        edge.right = y
    else:
        edge.left = y
        edge.right = x
    pq.append(edge)
    pq.sort(key = lambda x: x.data)


tree = pq[-1]

# TREE

#        100
#       /    \
#     a:45    55
#           /     \
#         25       \
#        /  \       \
#       c:12  b:13   30
#                   /  \
#                 14   d:16
#                /  \
#              f:5   e:9


# Decompression

def decompress(root, s):
    current = root
    for i in s:
        if i=="0":
            current = current.left
        else:
            current = current.right
    ans = "Node"
    for key, val in d.items():
        if val==current.data:
            ans = key

    print(ans, current.data)

decompress(tree, "1101")
# output = e 9
