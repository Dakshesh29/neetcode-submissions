class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        h = len(nums) - 1

        while l < h:
            if nums[l] %2 == 0:
                l+=1 
            elif nums[h] %2 != 0:
                h-=1
            else:
                nums[l],nums[h] = nums[h],nums[l]
                l+=1
                h-=1
        return  nums

