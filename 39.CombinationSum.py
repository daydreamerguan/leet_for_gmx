class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        dp_list = [[[],], ]
        for cnt_target in range(1, target + 1):
            cnt_result_list = []
            for cnt_cand in candidates:
                prev_target = cnt_target - cnt_cand
                if prev_target < 0 or len(dp_list[prev_target]) == 0:
                    continue
                prev_results = dp_list[prev_target]
                for prev_result in prev_results:
                    if not(prev_result) or prev_result[0] >= cnt_cand:
                        new_result = [cnt_cand,]
                        new_result.extend(prev_result)
                        cnt_result_list.append(new_result)
            dp_list.append(cnt_result_list)
        return dp_list[-1]

if __name__ == '__main__':
    print Solution().combinationSum([2,3,6,7], 7)
    print Solution().combinationSum([2,3,5], 8)
    print Solution().combinationSum([2], 1)
    print Solution().combinationSum([1], 1)
    print Solution().combinationSum([1], 2)
    print Solution().combinationSum([1], 3)
    print Solution().combinationSum([1, 2], 10)