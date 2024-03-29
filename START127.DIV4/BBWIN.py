import math
t = int(input())
for i in range(t):
    a,b=map(int,input().split())
    diff = a - b
    if diff >= 10:
        print(0)
    else:
        rem = 10 - diff
        print(math.ceil(rem/3))


# input:

''''
3
11 2
100 23
3 5
'''