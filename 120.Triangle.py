class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        triangle_size = len(triangle)
        triangle_min_sums = []
        for i in xrange(0, triangle_size):
            cnt_line = triangle[i]
            cnt_min_sums = []
            if i == 0:
                cnt_min_sums.append(cnt_line[0])
                triangle_min_sums.append(cnt_min_sums)
                continue
            prev_line_size = len(triangle[i - 1])
            for j, tri_value in enumerate(cnt_line):
                adj_left_index = j - 1
                adj_right_index = j
                new_value = None
                if j - 1 < 0:
                    new_value = triangle_min_sums[i - 1][adj_right_index] + tri_value
                elif adj_right_index >= prev_line_size:
                    new_value = triangle_min_sums[i - 1][adj_left_index] + tri_value
                else:
                    new_value = min(triangle_min_sums[i - 1][adj_right_index], triangle_min_sums[i - 1][adj_left_index]) + tri_value
                cnt_min_sums.append((new_value))
            triangle_min_sums.append(cnt_min_sums)
        return min(triangle_min_sums[-1])
