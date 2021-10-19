class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_height_left = 0
        dp_height = []
        for item in height:
            max_height_left = max(max_height_left, item)
            dp_height.append(max_height_left)
            max_height_right = 0
        index = len(height) - 1
        result = 0
        while index > 0:
            max_height_right = max(max_height_right, height[index])
            min_max_height = min(dp_height[index], max_height_right)
            if min_max_height > height[index]:
                result += (min_max_height - height[index])
            index -= 1
        return result