class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1,n+1):
            adj[i] = []
        
        for ui,vi,ti in times:
            adj[ui].append((vi,ti))
        
        mini = set()
        minHeap = [(0,k)]
        t = 0
        while minHeap:
            w1,n1 = heapq.heappop(minHeap)
            if n1 in mini:
                continue
            mini.add(n1)
            t = w1

            for n2,w2 in adj[n1]:
                if n2 not in mini:
                    heapq.heappush(minHeap,(w1+w2,n2))
        return t if len(mini) == n else -1