class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        max_limit = 45
        if n > 45:
            return []
        candidates = [i for i in range(1, 10)]
        dp_list = [[([], -1)], ]
        for cnt_target in range(1, n + 1):
            cnt_result_list = []

            for index, cnt_cand in enumerate(candidates):
                
                prev_target = cnt_target - cnt_cand
                if prev_target < 0 or len(dp_list[prev_target]) == 0:
                    continue
                prev_results = dp_list[prev_target]
                for prev_result in prev_results:
                    # []
                    if not(prev_result) or prev_result[1] >= index:
                        continue
                    if index >= 1 and cnt_cand == candidates[index - 1] and (prev_result[1] != index - 1  or prev_result[1] == -1 ) :
                        continue
                    new_result = list(prev_result[0])
                    new_result.append(cnt_cand)

                    cnt_result_list.append((new_result, index))
            dp_list.append(cnt_result_list)
        result = []
        for item in dp_list[-1]:
            if len(item[0]) == k:
                result.append(item[0])
        return result

if __name__ == '__main__':
    print(Solution().combinationSum3(3, 7))
    print(Solution().combinationSum3(3, 9))
    print(Solution().combinationSum3(4, 1))