class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        simplify = set(nums)
        if len(simplify) < len(nums):
            return True
        return False
            
        