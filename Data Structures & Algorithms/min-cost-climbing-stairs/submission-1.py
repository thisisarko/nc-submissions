class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        for i in range(len(cost)):
            if i == 0 or i == 1:
                dp[i] = cost[i]
            else:
                dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        return min(dp[-1], dp[-2])
        