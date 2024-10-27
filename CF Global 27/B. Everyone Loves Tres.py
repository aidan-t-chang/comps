from itertools import product

def smallest(n):
    if n == 1:
        return -1 
    
    for c in product('36', repeat=n-1):
        num = ''.join(c) + '6'
        if is_valid(num):
            return int(num)
    return -1

def is_valid(n):
    sum_digits = sum(int(digit) for digit in n) # divisibility by 3
    if sum_digits % 3:
        return False
    
    odd = sum(int(n[i]) for i in range(0, len(n), 2))
    even = sum(int(n[i]) for i in range(1, len(n), 2))
    
    if (odd - even) % 11: # divisibility by 11
        return False
    
    return True


t = int(input())


for _ in range(t):
    n = int(input())
    print(smallest(n))