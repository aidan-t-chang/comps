def solve():
    n = int(input())
    arr = []
    res = [0] * (2 * n)
    all = set()
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(len(row)):
            res[i+j+1] = row[j]
            all.add(row[j])
    
    for i in range(len(res)):
        if res[i] == 0:
            for num in range(1, 2*n+1):
                if num not in all:
                    res[i] = num
                    break
    res_string = ""
    for n in res:
        res_string += str(n) + " "
    return res_string


t = int(input())
for _ in range(t):
    print(solve())





