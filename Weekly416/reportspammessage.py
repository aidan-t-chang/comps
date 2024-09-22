# You are given an array of strings message and an array of strings bannedWords.

# An array of words is considered spam if there are at least two words in it that 
# exactly match any word in bannedWords.

# Return true if the array message is spam, and false otherwise.


class Solution:
    def reportSpam(self, message, bannedWords) -> bool:
        counter = 0
        
        banned = set() # set for preventation against TLE (O(1) average lookup)
        for b in bannedWords:
            banned.add(b)

        for m in message:
            if m in banned:
                counter += 1
            if counter > 1:
                return True
        return False