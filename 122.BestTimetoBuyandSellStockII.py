class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profits_list = []
        price_size = len(prices)
        for i, price in enumerate(prices):
            if i == price_size - 1:
                continue
            profits_list.append(prices[i + 1] - price)

        profit = 0
        for i in profits_list:
            if i > 0:
                profit += i
        return profit