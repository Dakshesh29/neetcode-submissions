class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        h = len(heights)-1
        max_area = 0
        while l<h:
            if heights[l] < heights[h]:
                width = h - l
                height = min(heights[l],heights[h])
                area = width*height
                l+=1
                if max_area < area :
                    max_area = area
            else:
                width = h - l
                height = min(heights[l],heights[h])
                area = width*height
                h-=1
                if max_area < area :
                    max_area = area
        return max_area