class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        prefix = 0
        for i in range(len(nums)):
            if prefix == (tot - prefix - nums[i]):
                return i
            prefix += nums[i]            
        return -1
        