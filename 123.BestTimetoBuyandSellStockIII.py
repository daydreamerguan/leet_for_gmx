class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        global_dp_list = []
        local_dp_list = []
        # exchange time 0 1 2
        len_prices = len(prices)
        for i in xrange(0, 3):
            global_dp_list.append([0 for j in xrange(0, len_prices)])
            local_dp_list.append([0 for j in xrange(0, len_prices)])
        for i in xrange(1, 3):
            for j in xrange(1, len_prices):
                diff = prices[j] - prices[j - 1]
                local_dp_list[i][j] = max(global_dp_list[i - 1][j - 1] + diff, local_dp_list[i][j - 1] + diff);
                global_dp_list[i][j] = max(local_dp_list[i][j], global_dp_list[i][j - 1])

        return global_dp_list[2][len_prices - 1] 