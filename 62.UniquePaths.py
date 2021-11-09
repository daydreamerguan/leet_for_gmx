class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result_dict = {}
        return self.findPath(m, n, result_dict)

    def findPath(self, m, n, result_dict):
        if m == 1 and n == 1:
            return 1

        if (m, n) in result_dict:
            return result_dict[m, n]

        result = 0
        if m > 1:
            result += self.findPath(m - 1, n, result_dict)

        if n > 1:
            result += self.findPath(m, n - 1, result_dict)

        result_dict[(m, n)] = result
        return result

if __name__ == '__main__':
    print Solution().uniquePaths(7, 3)
    print Solution().uniquePaths(3, 2)
    print Solution().uniquePaths(3, 3)

