class Interval(object):
        def __init__(self, value, state):
            self.v = value
            self.state = state

def cmpInervals(a, b):
    v_res = cmp(a.v, b.v)
    if v_res != 0:
        return v_res
    else:
        return cmp(a.state, b.state)

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        interval_list = []
        for i in intervals:
            interval_list.append(Interval(i[0], 0))
            interval_list.append(Interval(i[1], 1))
        interval_list.append(Interval(newInterval[0], 0))
        interval_list.append(Interval(newInterval[1], 1))
        interval_list.sort(cmp=cmpInervals)
        cnt_stack = []
        result_list = []
        for interval in interval_list:
            # print interval.v, interval.state, cnt_stack
            if interval.state == 0:
                cnt_stack.append(interval.v)   
            else:
                cnt_start = cnt_stack.pop()
                if not cnt_stack:
                    result_list.append([cnt_start, interval.v])

        return result_list
        