class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur, sub = [],[]
        def help(i):
            if i>=len(nums):
                sub.append(cur.copy())
                return
            
            cur.append(nums[i])
            help(i+1)
            cur.pop()
            help(i+1)
        help(0)
        return sub