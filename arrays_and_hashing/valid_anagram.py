class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for letter in t:
            if letter not in s or s.count(letter) != t.count(letter):
                return False

        return True
