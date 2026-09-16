class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1
        while l < r :
            if heights[l] < heights[r]:
                width = r-l
                h = min(heights[l],heights[r])
                area = h * width
                l+=1
                if max_area < area:
                    max_area = area
            else:
                width = r-l
                h = min(heights[l],heights[r])
                area = h * width
                r-=1
                if max_area < area:
                    max_area = area
        return max_area