# You are given a string s.

# We define the mirror of a letter in the English alphabet as its corresponding letter 
# when the alphabet is reversed. For example, the mirror of 'a' is 'z', and the mirror of 'y' is 'b'.

# Initially, all characters in the string s are unmarked.

# You start with a score of 0, and you perform the following process on the string s:

# Iterate through the string from left to right.
# At each index i, find the closest unmarked index j such that j < i and s[j] is the mirror of s[i]. 
# Then, mark both indices i and j, and add the value i - j to the total score.
# If no such index j exists for the index i, move on to the next index without making any changes.
# Return the total score at the end of the process.

class Solution:
    def calculateScore(self, s: str) -> int:
        mirror = {chr(97+i):chr(122-i) for i in range(26)}
        res = 0

        previous = []
        marked = [False] * len(s)
        for i, char in enumerate(s):
            if marked[i]:
                continue
            else:
                if mirror[char] not in previous:
                    previous.append(char)
                else:
                    for j in range(i-1, -1, -1):
                        if s[j] == mirror[char] and not marked[j]:
                            marked[j] = True
                            marked[i] = True
                            res += (i - j)
                            break
        return res