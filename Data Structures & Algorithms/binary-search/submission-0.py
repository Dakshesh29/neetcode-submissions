class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        m = (l+r)//2
        result = -1
        while(l<r):
            if nums[m]<target:
                l = m+1
                result = m
            else:
                r = m-1
        return result

