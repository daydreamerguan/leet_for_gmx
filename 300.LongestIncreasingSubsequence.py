def find_not_less_index(left, right, dynamic_list, check_value, ret):
    if(right < left):
        return
    mid = int((left + right) / 2)
    cnt_value = dynamic_list[mid]
    if cnt_value >= check_value:
        ret[0] = mid
        find_not_less_index(left, mid - 1, dynamic_list, check_value, ret)
    else:
        find_not_less_index(mid + 1, right, dynamic_list, check_value, ret)


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dynamic_list = []
        for num in nums:
            # print(dynamic_list)
            if len(dynamic_list) == 0 or dynamic_list[-1] < num:
                dynamic_list.append(num)
            else:
                ret = [len(dynamic_list) - 1]
                find_not_less_index(0, len(dynamic_list) - 1, dynamic_list, num, ret)
                dynamic_list[ret[0]] = num
        return len(dynamic_list)


if __name__ == '__main__':
    # print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
    # print(Solution().lengthOfLIS([0,1,0,3,2,3]))
    # print(Solution().lengthOfLIS([7,7,7,7,7,7,7]))
    print(Solution().lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]))
    [10,9,2,5,3,4]