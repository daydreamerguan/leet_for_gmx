class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        say_list = ["1",]
        while len(say_list) < 30:
            say_list.append(self.CountAndSayFromPrev(say_list[-1]))

        return say_list[n - 1]

    def CountAndSayFromPrev(self, last_str):
        cnt_str = ""
        cnt_count = 0
        last_str_length = len(last_str)
        cnt_index = 0
        output_list = []
        while cnt_index < last_str_length:
            if cnt_str != last_str[cnt_index]:
                if cnt_count > 0:
                    output_list.append(str(cnt_count))
                    output_list.append(cnt_str)
                cnt_str = last_str[cnt_index]
                cnt_count = 1
            else:
                cnt_count += 1
            cnt_index += 1
        output_list.append(str(cnt_count))
        output_list.append(cnt_str)
        return "".join(output_list)
        
if __name__ == '__main__':
    for i in xrange(1, 9):
        print Solution().countAndSay(i)