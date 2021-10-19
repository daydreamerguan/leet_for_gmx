class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_length = len(nums)
        if nums_length == 1:
            return 0
        to_visit_index_range = (0, 1)
        cnt_step = 1
        while True:
            next_max = 0
            for cnt_index in xrange(to_visit_index_range[0], to_visit_index_range[1]):
                cnt_max_step = nums[cnt_index]
                max_reach = cnt_index + cnt_max_step
                if max_reach >= nums_length - 1:
                    return cnt_step
                if max_reach < to_visit_index_range[1]:
                    continue
                next_max = max(next_max, max_reach)
            to_visit_index_range = (to_visit_index_range[1], next_max + 1)
            assert(to_visit_index_range[1] > to_visit_index_range[0])
            cnt_step += 1

if __name__ == '__main__':
    print Solution().jump([2,3,1,1,4])
    print Solution().jump([2,3,0,1,4])
    print Solution().jump([5,9,3,2,1,0,2,3,3,1,0,0])
    print Solution().jump([1, 2, 3])
