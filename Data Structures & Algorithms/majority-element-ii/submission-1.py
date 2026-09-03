class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        map = {}
        res = []

        for num in nums:
            map[num] = map.get(num,0)+1

        for num,index in map.items():
            if index > n:
                res.append(index)

        return res