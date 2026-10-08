class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = [[]]
        for n in nums:
            nextP = []
            for p in perm:
                for i in range(len(p)+1):
                    if i>0 and p[i-1] == n:
                        break
                    pC = p.copy()
                    pC.insert(i,n)
                    nextP.append(pC)
            perm = nextP
        return perm