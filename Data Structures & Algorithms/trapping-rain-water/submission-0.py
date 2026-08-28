"""
To find the max area of water, we need to find the max height of water
that can be trapped at each index position.

This can be calculated by the relation:
water_height(i) = min(max_bar_height_left, max_bar_height_right) - height(i)

O(n) space solution: 
- Precompute maxLeft and maxRight arrays, each index containing the maximum height
to the left or right of that index.
- Compute min(maxLeft, maxRight) array

O(1) space solution: Use two pointers

The trick:
Notice what this relation means 

min(maxL, maxR)

If, while traversing from the ends of the structure,
maxL and maxR both are known, they can only increase as we move towards
the middle of the structure.
If we traverse from the end which is lower, we know that end will be the
bottleneck since we are taking the min and the other end can only increase.

"""


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        water = 0

        while l < r:
            if maxL <= maxR:
                l += 1
                water += max(maxL - height[l], 0)
                maxL = max(maxL, height[l])
            else:
                r -= 1
                water += max(maxR - height[r], 0)
                maxR = max(maxR, height[r])
        
        return water

        