class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        l = 0
        freq = 0
        count ={}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0)+1
            freq = max(freq,count[s[r]])

            while (r-l+1) - freq>k:
                count[s[l]] -= 1
                l+=1
            length = max(length, r -l+ 1)
        return length 
