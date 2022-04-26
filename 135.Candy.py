class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        size = len(ratings)
        candies = [1 for i in xrange(0, size)]
        for i in xrange(1, size):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        # print candies
        for i in xrange(size - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i - 1], candies[i] + 1)
        # print candies
        return sum(candies)  