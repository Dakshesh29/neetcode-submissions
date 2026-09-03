class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l = i+1 
            h = len(nums)-1
            while l<h:
                threesum = a + nums[l] + nums[h]
                if threesum > 0:
                    h-=1
                elif threesum < 0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[h]])
                    l+=1
                    while nums[l] == nums[l-1] and l<h:
                        l+=1
                        h-=1
        return res
                
        