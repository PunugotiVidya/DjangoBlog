
from itertools import combinations
from functools import reduce

n = int(input())
k = int(input())

inp = [int(input()) for i in range(n)]
def f(x, y): return x & y


cmb = []
for i in range(2, len(inp)+1):
    cmb.append(list(combinations(inp, i)))

cmb = list(cmb)
print(list(cmb))
res = 1
for lst in cmb:
    for i in lst:
        s = reduce(f, i)
        print(s)
        if s >= k and len(i) > res:
            res = len(i)
print(res)
