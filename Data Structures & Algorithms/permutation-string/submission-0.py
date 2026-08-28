class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1 = s1.lower()
        s2 = s2.lower()

        count_s1 = [0] * 26
        count_s2 = [0] * 26

        for c in s1:
            count_s1[ord(c) - ord('a')] += 1

        for c in s2[0:len(s1)]:
            count_s2[ord(c) - ord('a')] += 1
        
        l = 0
        r = len(s1) - 1

        while r < len(s2) - 1:
            if count_s1 == count_s2:
                return True
            

            count_s2[ord(s2[l]) - ord('a')] -= 1
            l += 1

            r += 1
            count_s2[ord(s2[r]) - ord('a')] += 1
        
        return count_s1 == count_s2

