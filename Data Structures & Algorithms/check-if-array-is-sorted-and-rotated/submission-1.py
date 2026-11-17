class Solution:
    def check(self, nums: List[int]) -> bool:
        n = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                n+=1
        
            if n>1:
                return False
        return True