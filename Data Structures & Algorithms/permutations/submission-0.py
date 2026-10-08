class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            nextperm = []
            for r in res:
                for j in range(len(r)+1):
                    rC = r.copy()
                    rC.insert(j,n)
                    nextperm.append(rC)
            res = nextperm
        
        return res