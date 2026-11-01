class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        pMap = {i: [] for i in range(n)}
        for v,e in edges:
            pMap[v].append(e)
            pMap[e].append(v)

        visit = set()

        def dfs(v, parent):
            if v in visit:
                return False

            visit.add(v)

            for nei in pMap[v]:
                if nei == parent:
                    continue

                if not dfs(nei, v):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n