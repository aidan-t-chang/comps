# cook your dish here
t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    rs = list(input().split())
    res = 0
    gun = 0
    for i in range(len(rs)):
        if gun == 0 and int(rs[i]) > d:
            res += 1
            gun = 1
        elif gun == 1 and int(rs[i]) <= d:
            res += 1
            gun = 0
    print(res)