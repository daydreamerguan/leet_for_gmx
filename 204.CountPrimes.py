class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        number_list = [0 for i in xrange(0, n)]
        prime_list = []
        for i in xrange(2, n):
            if number_list[i] != 0:
                continue
            prime_list.append((i))
            self.mark_prime(number_list, i, n)
        return len(prime_list)

    def mark_prime(self, number_list, k, n):
        index = k
        while index < n:
            number_list[index] = 1
            index += k


    def is_prime(self, n, prime_list):
        if n == 0 or n == 1:
            return False
        for prime in prime_list:
            if prime ** 2 > n:
                return True
            if n % prime == 0:
                return False
        return True
