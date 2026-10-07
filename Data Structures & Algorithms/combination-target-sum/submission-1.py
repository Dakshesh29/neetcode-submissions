class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        comb, cur = [],[]
        def help(i,total):
            if total == target:
                comb.append(cur.copy())
                return 
            for j in range(i,len(nums)):
                if total + nums[j]>target:
                    return 
                cur.append(nums[j])
                help(j,total+nums[j])
                cur.pop()
        help(0,0)
        return comb