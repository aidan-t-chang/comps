t = int(input())

for _ in range(t):
    s = str(input())
    for i in range(len(s)-2):
        if s[i] == s[i+1]:
            for c in range(26):
                if s[i] != chr(c):
                    s = s[0:i] + chr(c) + s[i+1:]
                    print(s)
                    break
'''
        elif i+1 == len(s):
            for c in range(26):
                if s[i] != chr(c):
                    s = s[0:i] + chr(c) + s[i+1:]
                    print(s)
                    break
'''