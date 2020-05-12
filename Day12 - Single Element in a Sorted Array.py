class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        vb = []
        for v in nums:
            if nums.count(v) == 1:
                return v
            elif v in vb:
                continue
            else:
                vb.append(v)
            
        
        