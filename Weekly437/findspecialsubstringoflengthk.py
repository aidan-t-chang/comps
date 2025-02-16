# You are given a string s and an integer k.

# Determine if there exists a substring of length exactly k in s that satisfies the following conditions:

# The substring consists of only one distinct character (e.g., "aaa" or "bbb").
# If there is a character immediately before the substring, it must be different from the character in the substring.
# If there is a character immediately after the substring, it must also be different from the character in the substring.
# Return true if such a substring exists. Otherwise, return false.

# A substring is a contiguous non-empty sequence of characters within a string.

class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        for r in range(k-1, len(s)):
            prev = s[r]
            check = True
            print(s[r-k+1:r+1])
            if all(char == prev for char in s[r-k+1:r+1]):
                if r-k >= 0:
                    if s[r-k] != prev:
                        pass
                    else:
                        check = False
                if r + 1 < len(s):
                    if s[r+1] != prev:
                        pass
                    else:
                        check = False
                if check:
                    return True
        return False