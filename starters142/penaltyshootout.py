t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    if 0 <= x-y < 2:
        print('yes')
    elif 0 <= y-x < 3:
        print('yes')
    else:
        print('no')