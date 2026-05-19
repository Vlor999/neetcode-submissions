class Solution:
    def trap(self, heights):
        volume = 0
        if heights == []:
            return volume
        
        left, right = 0, len(heights) - 1
        maxLeft, maxRight = heights[left], heights[right]

        while left < right:
            if maxLeft < maxRight:
                maxLeft = max(maxLeft, heights[left + 1])
                volume += max(0, maxLeft - heights[left+1])
                left += 1
            else:
                maxRight = max(maxRight, heights[right - 1])
                volume += max(0, maxRight - heights[right - 1])
                right -= 1
        return volume
        