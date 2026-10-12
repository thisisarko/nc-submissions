"""
max_money[i] = max(nums[i] + max_money[i-2], max_money[i-1])

nums = [2,9,8,3,6]

1: dp = [2,9,10]
2: dp = [2,9,10,12]
3: dp = [2,9,10,12,16]

[2,1,1,2]

dp: [2,2,3,4]
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        dp = [
            nums[0],
            max(nums[0], nums[1])
        ]

        for i in range(2, len(nums)):
            prev_max = dp[-1]
            current_max = max(nums[i] + dp[-2], prev_max)
            dp[-1] = current_max
            dp[-2] = prev_max
        return dp[-1]
        
