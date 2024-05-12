# You are given two strings s and t such that every character occurs at most once in s and t is a permutation of s.
# The permutation difference between s and t is defined as the sum of 
# the absolute difference between the index of the occurrence of each character in 
# s and the index of the occurrence of the same character in t.
# Return the permutation difference between s and t.

def find(s, t):
    dicS = {}
    dicT = {}
    for i in range(len(s)):
        dicS[s[i]] = i
    for i in range(len(t)):
        dicT[t[i]] = i

    res = 0
    for key in dicS:
        res += abs(dicS[key] - dicT[key])
    
    return res


print(find("abc", "bac"))

