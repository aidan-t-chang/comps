def solve():
    n, m, l, r = map(int, input().split())
    # m-th day has a segment of length m

    while m != n:
        if abs(l - 0) > abs(r - 0):
            l += 1
        else:
            r -= 1
        n -= 1

    ret = str(l) + " " + str(r) 
    return ret


t = int(input())
for _ in range(t):
    print(solve())


