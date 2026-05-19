class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = float("-inf")
        while left < right:
            curr_area = min(heights[left], heights[right]) * (right - left)
            area = max(curr_area, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return area
