class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights_Length = len(heights)
        max_area = [0 for x in xrange(0, heights_Length)]
        heights_stack = []
        max_area = 0
        for index, height in enumerate(heights):
            left = index
            while heights_stack and heights_stack[-1][1] > height:
                item = heights_stack.pop()
                width = index - item[0]
                cnt_max_area = width * item[1]
                left = item[0]
                if cnt_max_area > max_area:
                    max_area = cnt_max_area
            heights_stack.append((left, height))

        while heights_stack:
            item = heights_stack.pop()
            cnt_max_area = 0
            width = heights_Length - item[0]
            cnt_max_area = width * item[1]
            if cnt_max_area > max_area:
                max_area = cnt_max_area
        return max_area

if __name__ == '__main__':
    print Solution().largestRectangleArea([2, 4])