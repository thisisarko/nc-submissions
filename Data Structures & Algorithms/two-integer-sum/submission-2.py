class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            num = nums[i]
            lookup[target - num] = i
        for i in range(len(nums)):
            num = nums[i]
            if num in lookup and lookup[num] != i:
                return sorted([i, lookup[num]])