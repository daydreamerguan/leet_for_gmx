class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height_length = len(height)
        left = 0
        right = height_length - 1
        max_area = 0
        cnt_max = 0
        while(left < right):
            next_left = left
            next_right = right
            if height[left] >= height[right]:
                next_right -= 1
            else:
                next_left += 1
            cnt_max = min(height[left], height[right]) * abs(right - left)
            if cnt_max > max_area:
                max_area = cnt_max
            left = next_left
            right = next_right
        return max_area

if __name__ == '__main__':
   print Solution().maxArea([1,8,6,2,5,4,8,3,7])