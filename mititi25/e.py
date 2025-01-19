def mex(arr, n):
    arr2 = [i for i in range(1, n+1)]
    for num in arr2:
        if num not in arr:
            return num+1


def solve():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 2:
            print(mex(arr[query[1]:query[2]+1], len(arr)))
        else:
            arr[query[1]-1] = query[2]
            
solve()