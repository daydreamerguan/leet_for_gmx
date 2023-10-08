class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        len_points = len(points)
        if len_points == 0:
            return 0
        if len_points == 1:
            return 1
        line_dict = {}
        for i in xrange(0, len_points):
            for j in xrange(i + 1, len_points):
                a, b, c = self.get_line_pair(points[i], points[j])
                if a not in line_dict:
                    line_dict[a] = {}
                if b not in line_dict[a]:
                    line_dict[a][b] = {}
                if c not in line_dict[a][b]:
                    line_dict[a][b][c] = set()
                line_dict[a][b][c].add(i)
                line_dict[a][b][c].add(j)

        max_points = 0
        for a, item_0 in line_dict.iteritems():
            for b, item_1 in item_0.iteritems():
                for c, item_2 in item_1.iteritems():
                    cnt_size = len(item_2)
                    if cnt_size > max_points:
                        max_points = cnt_size
        return max_points

    def get_max_common_divisor(self, x, y):
        if x == 0:
            return y
        if y == 0:
            return x
        x = abs(x)
        y = abs(y)
        max_ = max(x, y)
        min_ = min(x, y)
        if max_ % min_ == 0:
            return min_
        else:
            return self.get_max_common_divisor(min_, max_ % min_)


    def get_line_pair(self, p1, p2):
        x_diff = p2[0] - p1[0]
        y_diff = p2[1] - p1[1]
        if x_diff < 0:
            x_diff = abs(x_diff)
            y_diff = -y_diff
        common_diff = self.get_max_common_divisor(x_diff, y_diff)
        x_diff /= common_diff
        y_diff /= common_diff
        axis_value = x_diff * p1[1] - y_diff * p1[0]
        return (x_diff, y_diff, axis_value)
