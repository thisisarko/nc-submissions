def sumsquare(n):
    a = n
    s = 0
    while a != 0:
        num = a % 10
        s += num*num
        a = a // 10

    return s

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        s = n
        while True:
            s = sumsquare(s)
            if s == 1:
                return True
            if s in seen:
                return False
            seen.add(s)
        
        