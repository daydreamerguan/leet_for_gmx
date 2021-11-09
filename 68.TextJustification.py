class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result_list = []
        cnt_result = [[], 0]
        for word in words:
            word_length = len(word)
            new_length = cnt_result[1] + word_length
            if cnt_result[0]:
                new_length += 1
            if new_length <= maxWidth:
                cnt_result[0].append(word)
                cnt_result[1] = new_length
            else:
                result_list.append(cnt_result[0])
                cnt_result = [[word], word_length]
        if cnt_result[0]:
            result_list.append(cnt_result[0])
        final_list = []
        for word_index, word_list in enumerate(result_list):
            cnt_list = []
            list_size = len(word_list)
            total_word_length = 0
            for word in word_list:
                total_word_length += len(word)
            cnt_list.append(word_list[0])
            rest_size = maxWidth - total_word_length
            if list_size == 1:
                if rest_size > 0:
                    cnt_list.append(" " * rest_size)
            elif word_index == len(result_list) - 1:
                for i in xrange(1, list_size):
                    cnt_list.append(" ")
                    cnt_list.append(word_list[i])
                last_space_length = rest_size - list_size + 1
                if last_space_length > 0:
                    cnt_list.append(" " * last_space_length)
            else:
                rest_mod = rest_size % (list_size - 1)
                rest_space_length = rest_size / (list_size - 1)
                for i in xrange(1, list_size):
                    cnt_length = rest_space_length;
                    if rest_mod > 0:
                        cnt_length += 1
                        rest_mod -= 1
                    cnt_list.append(" " * cnt_length)
                    cnt_list.append(word_list[i])
            result_string = "".join(cnt_list)
            assert len(result_string) == maxWidth
            final_list.append(result_string)
        return final_list

if __name__ == '__main__':
    result = Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20)
    for item in result:
        print item
    result = Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], 16)
    for item in result:
        print item
    result = Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
    for item in result:
        print item

    