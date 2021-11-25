class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s.isdigit():
            return []
        result_list = []
        self.restoreIpAddressesSolver(s, 0, result_list, [], len(s))
        return result_list

    
    def restoreIpAddressesSolver(self, s, start_index, result_list, cnt_result, slen):
        if len(cnt_result) == 4:
            if start_index == slen:
                ip_result = [str(x) for x in cnt_result]
                ip_result_str = ".".join(ip_result)
                result_list.append(ip_result_str)
            return
        max_length = 3
        for i in xrange(1, max_length + 1):
            end_index = start_index + i
            if end_index > slen:
                break
            if s[start_index] == "0" and i >= 2:
                break
            sub_str = s[start_index:end_index]
            ip_int = int(sub_str)
            if ip_int > 255 or ip_int < 0:
                continue
            cnt_result.append(ip_int)
            self.restoreIpAddressesSolver(s, end_index, result_list, cnt_result, slen)
            cnt_result.pop()

if __name__ == '__main__':
    print Solution().restoreIpAddresses("25525511135")
    print Solution().restoreIpAddresses("0000")
    print Solution().restoreIpAddresses("1111")
    print Solution().restoreIpAddresses("010010")
    print Solution().restoreIpAddresses("101023")
    print Solution().restoreIpAddresses("11111111")
    



