#Solution1
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        controlSet = set()
        for num in nums:
            if num in controlSet:
                return True
            controlSet.add(num)
        return False
    
#Solution2
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = set(nums)
        if len(hashMap) == len(nums):
            return False
        else:
            return True