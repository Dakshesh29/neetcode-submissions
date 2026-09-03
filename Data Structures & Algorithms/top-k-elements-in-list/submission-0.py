class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map ={}
        res = []

        for key,value in enumerate(nums):
            map[value] = 1+map.get(value,0)
        
        for key,value in map.items():
            if value >= k:
                res.append(key)
        return res
        