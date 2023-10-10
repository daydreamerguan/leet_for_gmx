class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        pre_map = {}
        sub_map = {}
        retain_course_set = set(range(0, numCourses))
        for sub, pre in prerequisites:
            if pre not in sub_map:
                sub_map[pre] = set()
            if sub not in pre_map:
                pre_map[sub] = set()
            sub_map[pre].add(sub)
            pre_map[sub].add(pre)
        first_level_items = set()
        for i in xrange(0, numCourses):
            if i not in pre_map:
                first_level_items.add(i)

        final_course_list = []
        while len(retain_course_set) > 0 and len(first_level_items) > 0:
            next_level_items = set()
            for i in first_level_items:
                if i in retain_course_set:
                    retain_course_set.remove(i)
                    final_course_list.append(i)
                if i in sub_map:
                    for j in sub_map[i]:
                        pre_map[j].remove(i)
                        if len(pre_map[j]) == 0:
                            del pre_map[j]
                            next_level_items.add(j)
                    del sub_map[i]
            first_level_items = next_level_items
        if len(retain_course_set) == 0:
            return final_course_list
        else:
            return []

