class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map ={}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            map[num] = 1+map.get(num,0)
        for n,c in map.items():
            freq[c].append(n)
        
        res = []

        for i in range(len(freq)-1, 0, -1):
            for i in freq[i]:
                res.append(i)
                if len(res) == k:
                    return res
        

        
        