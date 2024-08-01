# cook your dish here
a,b,c,x = map(int, input().split())
if a*b*c > x**3:
    print('cuboid')
elif a*b*c < x**3:
    print('cube')
else:
    print('equal')