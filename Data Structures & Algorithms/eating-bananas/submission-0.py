"""
len(piles) <= h, because for k_max = max(piles), it would take len(piles) hours
at least, i.e. 1 hour for each index in piles.

k :- [1, max(piles)]

"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h: return max(piles)

        def condition(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            return hours <= h
        
        l, r = 1, max(piles)
        while l < r:
            mid = l + (r-l) // 2
            if condition(mid):
                r = mid
            else:
                l = mid + 1
        return r


        