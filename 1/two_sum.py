class Solution:
    def __init__(self):
        self.hashtable={}
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remain=target-nums[i]
            if remain in self.hashtable:
                return [self.hashtable[remain],i]
            self.hashtable[nums[i]]=i
        return 