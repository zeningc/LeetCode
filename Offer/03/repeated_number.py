class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        if not nums:
            return
        c=dict()
        for i in nums:
            if c.get(i,0)==0:
                c[i]=1
            else:
                return i
        return