class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters = {}
        for c in s:
            characters[c] = characters.get(c, 0) + 1
        for c in t:
            if not characters.get(c):
                return False
            characters[c] -= 1
        if any(characters.values()):
            return False
        return True
