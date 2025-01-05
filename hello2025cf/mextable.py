t = int(input())

def solve():
    n, m = map(int, input().split())
    
    return max(n, m) + 1

for i in range(t):
    print(solve())