class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cur, sub = [],[]
        def help(i):
            if i>=len(nums):
                sub.append(cur.copy())
                return 
            
            cur.append(nums[i])
            help(i+1)
            cur.pop()
            while i+1< len(nums) and nums[i] == nums[i+1]:
                i+=1
            help(i+1)
        help(0)
        return sub