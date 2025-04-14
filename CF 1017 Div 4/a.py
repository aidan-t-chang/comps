def solve():
    n = int(input())
    for i in range(n):
        s1, s2, s3 = map(str, input().split())
        new = s1[0] + s2[0] + s3[0]
        print(new)
solve()
