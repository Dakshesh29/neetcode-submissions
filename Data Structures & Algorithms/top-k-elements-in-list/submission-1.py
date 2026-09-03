class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map ={}
        res = []

        for num in nums:
            map[num] = 1+map.get(num,0)
        
        for key,value in map.items():
            if value >= k:
                res.append(key)
        return res
        