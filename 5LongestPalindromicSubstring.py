class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.matcher(s)


    def matcher(self, s):
        character_num_array = [0, ]
        max_centric_len = 0
        max_left_bound = 0
        max_right_bound = 0
        for x in s:
            character_num_array.append(ord(x))
            character_num_array.append(0);

        array_len = len(character_num_array)
        for center in xrange(1, array_len - 1):
            cnt_half_len = 0
            left_bound = center
            right_bound = center
            while left_bound >= 0 and right_bound < array_len and  character_num_array[left_bound] == character_num_array[right_bound]:
                
                cnt_half_len += 1
                left_bound -= 1
                right_bound += 1
            cnt_length = cnt_half_len - 1
            left_bound = center - cnt_half_len + 1
            right_bound = center + cnt_half_len - 1
            '''
            if character_num_array[center] == 0:
                cnt_length = cnt_half_len - 1
            else:
                cnt_length = 2 * cnt_half_len - 3
            '''
            # print "center", center, "len", cnt_length, "cnt_half_len", cnt_half_len
            if cnt_length > max_centric_len:
                max_centric_len = cnt_length
                max_left_bound = left_bound
                max_right_bound = right_bound
        final_array = []
        index = max_left_bound
        while index <= max_right_bound:
            if character_num_array[index] != 0:
                final_array.append(chr(character_num_array[index]))
            index +=1
        return "".join(final_array)


if __name__ == '__main__':
    print Solution().longestPalindrome("aba")






        