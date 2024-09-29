# potentially greedy solution?

#keep finding largest power of k that can fit into n until n == 0 ?

import math

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    if k == 1 or n < k:
        print(n) 
        continue
    res = 0
    while n > 0:
        # calculate floor value of log base k of n
        power = math.floor(math.log(n, k)) # math.log(a, base)
        if k != 1:
            n -= k**power
        res += 1
    print(res)
