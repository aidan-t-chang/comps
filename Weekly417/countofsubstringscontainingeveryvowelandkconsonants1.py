# You are given a string word and a non-negative integer k.

# Return the total number of 
# substrings
# of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # sliding window?
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        def count_vowels(st): #finds # unique vowels in substring
            count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
            for char in st:
                if char in vowels:
                    count[char] += 1
            return all(count[c] > 0 for c in count)
            
        def count_consonants(st, k):
            res = 0
            for char in st:
                if char not in vowels:
                    res += 1
            return res == k

        res = 0

        l = 0
        right = 4+k
        while right - l >= 4+k:
            right = 4+k+l
            while right < len(word):
                if count_vowels(word[l:right+1]) and count_consonants(word[l:right+1], k):
                    res += 1
                right += 1
            l += 1
        return res
