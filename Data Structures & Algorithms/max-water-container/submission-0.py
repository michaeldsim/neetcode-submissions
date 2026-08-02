class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        largest = float('-inf')

        while left < right:
            height = min(heights[left], heights[right])
            largest = max(height * (right - left), largest)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return largest