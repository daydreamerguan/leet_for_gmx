class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary_str = "".join("{0:032b}".format(n)[::-1])
        return int(binary_str, 2)

if __name__ == '__main__':
    bin_num = b'00000010100101000001111010011100'
    Solution().reverseBits(int(bin_num, 2))