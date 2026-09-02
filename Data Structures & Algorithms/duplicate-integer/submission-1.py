class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}

        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1

        if any(value > 1 for value in dict.values()):
            return True
        else:
            return False