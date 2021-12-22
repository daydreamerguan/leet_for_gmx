class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        cnt_profit = 0
        cnt_max = prices[-1]
        index = len(prices) - 1
        while index >= 0:
            cnt_price = prices[index]
            if cnt_price > cnt_max:
                cnt_max = cnt_price
            if cnt_max - cnt_price > cnt_profit:
                cnt_profit = cnt_max - cnt_price
            index -= 1
        return cnt_profit