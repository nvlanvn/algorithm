class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            tmp = min(height[left], height[right])
            tmp = tmp * (right - left)
            if tmp > max_area:
                max_area = tmp
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area