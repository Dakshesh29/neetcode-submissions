class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        count = 0
        var = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    count+=1
                    var = nums[j]
                
            if count >= len(nums)/2:
                return nums[i]
        return var            