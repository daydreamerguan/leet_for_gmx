class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        valid_nums_dict = {}
        for num in nums:
            if num not in valid_nums_dict:
                valid_nums_dict[num] = 0
            valid_nums_dict[num] += 1
        res = []
        self.recursive_permute(valid_nums_dict, res, [], 0, len(nums))
        return res


    def add_res(self, final_res, res):
        add_res = [x for x in res]
        final_res.append(add_res)

    def recursive_permute(self, valid_nums_dict, res_list, cnt_res, cnt_len, max_len):
        if cnt_len == max_len:
            self.add_res(res_list, cnt_res)
            return

        keys = valid_nums_dict.keys()
        for key in keys:
            if valid_nums_dict[key] == 0:
                continue
            valid_nums_dict[key] -= 1
            cnt_res.append(key)
            self.recursive_permute(valid_nums_dict, res_list, cnt_res, cnt_len + 1, max_len)
            valid_nums_dict[key] += 1
            cnt_res.pop()

if __name__ == '__main__':
    print Solution().permuteUnique([1,2,3])
    print Solution().permuteUnique([1,1,2])