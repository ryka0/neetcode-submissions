class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        vals = {} # k: n, v: index i

        for i, n in enumerate(nums):
            if (target - n) in vals:
                return [vals[target-n],i]
            else:
                vals[n] = i


#Testing something            
        