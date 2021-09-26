# -*- coding: UTF-8 -*-
import Queue
class Solution(object):

    def popQueue(self, in_queue, word_remain_count_dict):
        word = in_queue.get_nowait()
        word_remain_count_dict[word] += 1


    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        words_count = len(words)
        if words_count == 0:
            return []
        ret_list = []
        words_set = set(words)
        word_length = len(words[0])
        word_remain_count_dict = {}
        
        for word in words:
            if word not in word_remain_count_dict:
                word_remain_count_dict[word] = 0
            # consider words has same word
            word_remain_count_dict[word] += 1
        len_str = len(s)
        for start_pos in xrange(0, word_length):
            cnt_start_pos = start_pos
            cnt_end_pos = cnt_start_pos + word_length
            valid_queue = Queue.Queue()
            matched_start_pos = -1
            while cnt_end_pos <= len_str:
                cnt_sub_str = s[cnt_start_pos:cnt_end_pos]
                # matched
                if cnt_sub_str in words_set:
                    # 没用空余的了
                    # print "cnt_sub_str", cnt_sub_str, "word_remain_count_dict", word_remain_count_dict,cnt_start_pos, cnt_end_pos
                    while word_remain_count_dict[cnt_sub_str] == 0:
                        self.popQueue(valid_queue, word_remain_count_dict)
                        matched_start_pos += word_length
                    if matched_start_pos == -1:
                        matched_start_pos = cnt_start_pos
                    valid_queue.put_nowait(cnt_sub_str)
                    word_remain_count_dict[cnt_sub_str] -= 1
                    if valid_queue.qsize() == words_count:
                        ret_list.append(matched_start_pos)
                else:
                    cnt_queue_size = valid_queue.qsize()
                    for x in xrange(0, cnt_queue_size):
                        self.popQueue(valid_queue, word_remain_count_dict)
                    matched_start_pos = -1
                cnt_start_pos += word_length
                cnt_end_pos += word_length
            cnt_queue_size = valid_queue.qsize()
            for x in xrange(0, cnt_queue_size):
                self.popQueue(valid_queue, word_remain_count_dict)
        return ret_list

if __name__ == '__main__':
    print Solution().findSubstring("ababababab", ["ababa","babab"])
    print Solution().findSubstring("barfoothefoobarman", ["foo","bar"])
    print Solution().findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])
    print Solution().findSubstring("wordgoodgoodgoodbestword",  ["word","good","best","word"])

