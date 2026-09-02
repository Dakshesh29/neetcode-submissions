class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map1,map2 = {},{}

        for i in range(len(s)):
            map1[s[i]] = 1+ map1.get(s[i],0)
            map2[t[i]] = 1+ map2.get(t[i],0)
        
        for i in map1:
            if map1[i] != map2.get(i,0):
                return False
        return True