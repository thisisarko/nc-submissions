from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(lambda: 0)
        for i in s:
            count[i]+=1
        for i in t:
            count[i]-=1
        
        for val in count.values():
            if val != 0:
                return False
        
        return True
