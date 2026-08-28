class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_s1, count_s2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1
        
        matches = sum(count_s1[i] == count_s2[i] for i in range(26))

        l = 0
        r = len(s1) - 1

        while r < len(s2) - 1:
            if matches == 26:
                return True
            
            left = ord(s2[l]) - ord('a')
            count_s2[left] -= 1

            if count_s1[left] == count_s2[left]:
                # gained a match after removal
                matches += 1
            elif count_s1[left] == count_s2[left] + 1:
                # lost a match
                matches -= 1
            else:
                # neither gained or lost a match
                pass

            l += 1

            r += 1
            right = ord(s2[r]) - ord('a')
            count_s2[right] += 1

            if count_s1[right] == count_s2[right]:
                matches += 1
            elif count_s1[right] + 1 == count_s2[right]:
                matches -= 1
            else:
                pass
        
        return matches == 26
