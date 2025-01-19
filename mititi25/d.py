def solve():
    n, k = map(int, input().split())
    arr = []
    
    for _ in range(n):
        ss = list(map(int, input().split()))
        arr.append(ss)
    
    ordering = {}
    alt = arr.copy()
    
    f = False
    arr.sort()
    for i in range(len(arr)):
        for j in range(len(alt)):
            if arr[i] == alt[j]:
                ordering[i] = j + 1
                
    for i in range(1, len(arr)):
        for j in range(1, k):
            if arr[i][j] < arr[i-1][j]:
                f = True
                break
        if f:
            break
    
    if f:
        print("NO")
        return
    
    print("YES")
    return_str = ""
    for i in range(len(arr)):
        return_str += str(ordering[i]) + " "
    print(return_str)    
    
solve()