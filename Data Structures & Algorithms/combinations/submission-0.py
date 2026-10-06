class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        cur, comb = [],[]
        def help(i):
            if len(cur)==k:
                comb.append(cur.copy())
                return
            if i>n:
                return 
            
            cur.append(i)
            help(i+1)
            cur.pop()
            help(i+1)
        help(1)
        return comb