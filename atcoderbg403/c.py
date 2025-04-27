def solve():
    n, m, q = map(int, input().split())
    users = [set() for _ in range(n)]
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            y = query[2]
            users[x-1].add(y)
        elif query[0] == 2:
            x = query[1]
            for j in range(1, m+1):
                users[x-1].add(j)
        else:
            x = query[1]
            y = query[2]
            print('Yes') if y in users[x-1] else print('No')


solve()
