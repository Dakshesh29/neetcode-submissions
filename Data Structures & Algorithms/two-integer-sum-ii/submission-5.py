class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) - 1
        sum = 0
        res = []

        while l<r:
            sum = numbers[l]+numbers[r]
            if sum == target:
                res.append(l+1)
                res.append(r+1)
                return res
            elif sum < target:
                l +=1
            else:
                r -=1

        return res