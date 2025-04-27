def solve():
    s1 = input()
    s2 = input()

    flag = True
    for i in range(0, len(s1)-len(s2)+1):
        sub = s1[i:i+len(s2)]
        for j in range(len(sub)):
            if sub[j] != "?" and sub[j] == s2[j]:
                flag = True
            elif sub[j] != "?" and sub[j] != s2[j]:
                flag = False
                break
    return "Yes" if flag else "No"


print(solve())
