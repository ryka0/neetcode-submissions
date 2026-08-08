class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        pSum = 0
        pCount = {0:1}

        for n in nums:
            pSum += n
            diff = pSum - k
            res += pCount.get(diff, 0)
            pCount[pSum] = 1 + pCount.get(pSum, 0)

        return res
        