class Solution(object):
    def maxArea(self, height):
        left = 0 
        right = len(height) - 1
        max_Area = 0


        while left < right :
            area = min(height[left] , height[right]) * (right - left)
            max_Area = max(max_Area , area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_Area




        