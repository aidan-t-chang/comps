t = int(input())
for i in range(t):
    n = int(input())
    p = n // 2 # sum of length and width have to be <= to this number
    l = n // 4 # get shape as close to a square as possible
    w = p - l
    print(l*w)