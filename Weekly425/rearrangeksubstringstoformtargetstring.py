# You are given two strings s and t, both of which are anagrams of each other, and an integer k.

# Your task is to determine whether it is possible to split the string s into k equal-sized substrings, rearrange the substrings, 
# and concatenate them in any order to create a new string that matches the given string t.

# Return true if this is possible, otherwise, return false.

# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

# A substring is a contiguous non-empty sequence of characters within a string

from collections import defaultdict

class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        if s == t:
            return True
            
        contention = []
        l = 0
        for r in range(len(s)//k, len(s)+1, len(s)//k):
            contention.append(s[l:r])
            l = r

        count = defaultdict(int)
        for sub in contention:
            count[sub] += 1

        comparison = []
        l = 0
        for r in range(len(t)//k, len(t)+1, len(t)//k):
            comparison.append(t[l:r])
            l = r
        
        for c in comparison:
            if count[c] == 0:
                return False
            count[c] -= 1
        return True