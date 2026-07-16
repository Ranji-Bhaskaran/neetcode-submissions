class Solution:
    def maxArea(self, heights: List[int]) -> int:
        high = heights[0]
        area = 0
        for i, n in enumerate(heights):
            r = i+1
            while r< len(heights):
                ar = (r-i) * min(n, heights[r])
                area = max(area, ar)
                r+=1
        return area