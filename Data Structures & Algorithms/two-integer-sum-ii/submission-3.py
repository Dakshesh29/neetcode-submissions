class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        h = len(numbers) -1 
        sum = 0
        ans = []
        while(l<h):
            sum = numbers[l]+numbers[h]
            if sum == target:
                ans.append(l+1)
                ans.append(h+1)
                return ans
            elif sum<=target:
                l+=1
            else:
                h-=1
        
        return ans