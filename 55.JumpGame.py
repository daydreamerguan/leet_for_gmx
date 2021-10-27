class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_length = len(nums)
        if nums_length == 1:
            return True
        to_visit_index_range = (0, 1)
        cnt_step = 1
        while True:
            next_max = 0
            # print to_visit_index_range
            for cnt_index in xrange(to_visit_index_range[0], to_visit_index_range[1]):
                cnt_max_step = nums[cnt_index]
                max_reach = cnt_index + cnt_max_step
                if max_reach >= nums_length - 1:
                    return True
                if max_reach < to_visit_index_range[1]:
                    continue
                next_max = max(next_max, max_reach)
            to_visit_index_range = (to_visit_index_range[1], next_max + 1)
            if (to_visit_index_range[1] <= to_visit_index_range[0]):
                return False
            cnt_step += 1

if __name__ == '__main__':
    print Solution().canJump([2,3,1,1,4])
    print Solution().canJump([3,2,1,0,4])
    print Solution().canJump([0])
    print Solution().canJump([0, 1])
