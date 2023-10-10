class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        rect1_area = self.compute_rect_area(ax1, ay1, ax2, ay2)
        rect2_area = self.compute_rect_area(bx1, by1, bx2, by2)
        rect1_points = self.get_rect_point_list(ax1, ay1, ax2, ay2)
        rect2_points = self.get_rect_point_list(bx1, by1, bx2, by2)
        total_area = rect1_area + rect2_area
        rect1_hit_indexes = []
        rect2_hit_indexes = []
        for index, p in enumerate(rect1_points):
            x, y = p
            if self.is_point_in_rect(bx1, by1, bx2, by2, x, y):
                rect1_hit_indexes.append(index)

        for index, p in enumerate(rect2_points):
            x, y = p
            if self.is_point_in_rect(ax1, ay1, ax2, ay2, x, y):
                rect2_hit_indexes.append(index)

        if len(rect1_hit_indexes) == 1:
            # print(111)
            total_area -= self.get_one_hit_rect_area(rect1_points, rect2_points, rect1_hit_indexes[0])
            # print(222)
        elif len(rect1_hit_indexes) == 2:
            # print(333)
            total_area -= self.get_two_hit_rect_area(rect1_points, rect2_points, *rect1_hit_indexes)
        elif len(rect2_hit_indexes) == 2:
            # print(444)
            total_area -= self.get_two_hit_rect_area(rect2_points, rect1_points, *rect2_hit_indexes)
        elif len(rect1_hit_indexes) == 4:
            # print(555)
            total_area -= rect1_area
        elif len(rect2_hit_indexes) == 4:
            # print(666)
            total_area -= rect2_area
        elif self.is_special_corner(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
            total_area -= self.get_special_corner_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
            # print(777)
        return total_area

    ONE_HIT_RELATED_INDEX = {
        0: 2,
        1: 3,
        2: 0,
        3: 1,
    } 
    def get_one_hit_rect_area(self, rect_points, other_rect_points, hit_index):
        hit_x, hit_y = rect_points[hit_index]
        related_index = self.ONE_HIT_RELATED_INDEX[hit_index]

        other_x, other_y = other_rect_points[related_index]
        return self.compute_rect_area(hit_x, hit_y, other_x, other_y)

    def get_two_hit_rect_area(self, rect_points, other_rect_points, hit_index0, hit_index1):
        x1, y1 = rect_points[hit_index0]
        x2, y2 = rect_points[hit_index1]
        if hit_index0 == 0 and hit_index1 == 1:
            x2 = other_rect_points[2][0]
        elif hit_index0 == 1:
            y2 = other_rect_points[3][1]
        elif hit_index0 == 2:
            x2 = other_rect_points[0][0]
        else:
            y2 = other_rect_points[1][1]
        return self.compute_rect_area(x1, y1, x2, y2)

    def get_special_corner_area(self,  ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        return self.compute_rect_area(max(ax1, bx1), max(ay1, by1), min(ax2, bx2), min(ay2, by2))

    def is_special_corner(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        return (by2 >= ay2 and by1 <= ay1 and ax2 >= bx2 and ax1 <= bx1) or (ay2 >= by2 and ay1 <= by1 and bx2 >= ax2 and bx1 <= ax1)


    def get_rect_point_list(self, ax1, ay1, ax2, ay2):
        return [
            (ax1, ay1),
            (ax1, ay2),
            (ax2, ay2),
            (ax2, ay1),
        ]


    def compute_rect_area(self, ax1, ay1, ax2, ay2):
        return abs((ay2 - ay1) * (ax2 - ax1))


    def is_point_in_rect(self, ax1, ay1, ax2, ay2, x, y):
        return  ax1 <= x <= ax2 and ay1 <= y <= ay2

if __name__ == '__main__':
    Solution().computeArea(-5, -2, 5, 1, -3, -3, 3, 3)