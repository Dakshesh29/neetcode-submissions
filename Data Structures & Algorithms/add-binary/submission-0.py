class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = len(a) - 1
        h = len(b) - 1
        c = 0
        res = []
        while l>=0 or h>=0 or c:
            x = int(a[l]) if l>=0 else 0
            y = int(b[h]) if h>=0 else 0
            sum = x + y + c
            res.append(str(sum%2))  
            c = sum // 2

            l-=1
            h-=1
        return ''.join(res[::-1])