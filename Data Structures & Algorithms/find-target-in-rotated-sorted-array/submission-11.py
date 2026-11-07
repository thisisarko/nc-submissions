def find_min_idx(nums):
    l,r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid
    return l

def bsearch(nums, l, r, target):
    while l <= r:
        mid = (l+r) // 2
        if nums[mid] == target:
            return mid
        
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    
    return -1



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_idx = find_min_idx(nums)
        l,r = 0, len(nums) - 1
        if nums[min_idx] <= target <= nums[r]:
            return bsearch(nums, min_idx, r, target)
        else:
            return bsearch(nums, l, min_idx, target)
