class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        sum = 0
        l = 0
        h = len(nums)-1

        while(l<h):
            sum = nums[l]+nums[h]
            if sum == target:
                ans.append(l)
                ans.append(h)
                return ans
            elif sum<=target:
                l+=1
            else:
                h-=1
        return ans