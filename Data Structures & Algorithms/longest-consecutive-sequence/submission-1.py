class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_seq = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in s:
                start = nums[i]
                j = start + 1
                while j in s:
                    j += 1
                max_seq = max(max_seq, j - start)
        return max_seq




        