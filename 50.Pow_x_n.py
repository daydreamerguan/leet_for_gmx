class Solution(object):

    def internalPow(self, x, n, result_dict):
        if n < 0:
            return 1.0 / self.internalPow(x, -n, result_dict)
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n in result_dict:
            return result_dict[n]
        half_n = n / 2
        tail = n % 2
        half_ret = self.internalPow(x, half_n, result_dict)

        result = half_ret * half_ret * self.internalPow(x, tail, result_dict)
        result_dict[n] = result
        return result

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result_dict = {}
        return self.internalPow(x, n, result_dict)

if __name__ == '__main__':
    print Solution().myPow(2.000, 10)
    print Solution().myPow(2.100, 3) 
    print Solution().myPow(2.0, -2)