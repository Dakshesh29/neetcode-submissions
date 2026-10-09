class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res,sub = [],[]
        def help(i):
            if i>=len(s):
                res.append(sub.copy())
                return 
            
            for j in range(i,len(s)):
                if self.isPal(s,i,j):
                    sub.append(s[i:j+1])
                    help(j+1)
                    sub.pop()
        help(0)
        return res

    def isPal(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            
            l+=1
            r-=1
        return True