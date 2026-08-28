class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        n = len(nums)
        freq = [[] for i in range(n + 1)]
        for num, count in counts.items():
            freq[count].append(num)
        
        res = []
        for i in range(n, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
