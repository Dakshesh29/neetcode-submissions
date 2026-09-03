class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    count+=1
                
            if count >= len(nums)/2:
                return nums[i]
                    