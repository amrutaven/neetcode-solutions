class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights) - 1
        left = 0
        max_area = 0

        while (right > left):
            area = min(heights[right], heights[left]) * (right - left)
            max_area = max(max_area, area)
            if (heights[right] == heights[left]):
                right -= 1
                left += 1
            elif (heights[right] < heights[left]):
                right -= 1
            else:
                left += 1
            
        
        return max_area

        