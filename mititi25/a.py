t = int(input())

def solve():
    n = int(input())
    
    if 0 < n <= 5:
        return "MIT time"
    for i in range(13):
        if 5**i < n <= 5**(i+1):
            return "MIT^" + str(i+1) + " time"
        
        
for _ in range(t):
    print(solve())