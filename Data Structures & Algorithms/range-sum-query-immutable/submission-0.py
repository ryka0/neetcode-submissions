class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        tot = 0
        for n in nums:
            tot += n
            self.prefix.append(tot)
        
         

    def sumRange(self, left: int, right: int) -> int:
        sumR = self.prefix[right]
        sumL = self.prefix[left-1] if left > 0 else 0
        return(sumR - sumL) 
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)