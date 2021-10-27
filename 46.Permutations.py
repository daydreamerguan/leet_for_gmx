class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        valid_nums_set = set(nums)
        res = []
        self.recursive_permute(valid_nums_dict, res, [])
        return res


    def add_res(self, final_res, res):
        add_res = [x for x in res]
        final_res.append(add_res)

    def recursive_permute(self, valid_nums_set, res_list, cnt_res):
        if len(valid_nums_set) == 0:
            self.add_res(res_list, cnt_res)
            return

        cnt_valid_list = list(valid_nums_set)
        for item in cnt_valid_list:
            valid_nums_set.remove(item)
            cnt_res.append(item)
            self.recursive_permute(valid_nums_set, res_list, cnt_res)
            valid_nums_set.add(item)
            cnt_res.pop()

if __name__ == '__main__':
    print Solution().permute([1,2,3])