class Union:
    def __init__(self,n):
        self.par = list(range(n))
        self.rank = [1]*n

    def find(self,n):
        c = n
        while c != self.par[c]:
            self.par[c] = self.par[self.par[c]]
            c = self.par[c]
        return c
    
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pu,pv = pv,pu
        self.par[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = Union(n)
        res = n
        for u,v in edges:
            if dsu.union(u,v):
                res -=1
        return res        