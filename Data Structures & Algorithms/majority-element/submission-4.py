class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        var = None
        count = 0
        for n in nums:
            if count ==0:
                var = n

            if num == var:
                count +=1
            else:
                count -=1
        return var