class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        length = len(secret)
        guess_length = len(guess)
        min_length = min(len(guess), length)
        bull_mapping = {}
        sec_num_mapping = {}
        guess_num_mapping = {}
        for i in xrange(0, min_length):
            if secret[i] == guess[i]:
                bull_mapping[i] = secret[i]
        for i in xrange(0, length):
            sec_char = secret[i]
            if sec_char not in sec_num_mapping:
                sec_num_mapping[sec_char] = 0
            sec_num_mapping[sec_char] += 1
        for i in xrange(0, guess_length):
            guess_char = guess[i]
            if guess_char not in guess_num_mapping:
                guess_num_mapping[guess_char] = 0
            guess_num_mapping[guess_char] += 1
        bull_num = len(bull_mapping)
        for k, v in bull_mapping.iteritems():
            sec_num_mapping[v] -= 1
            guess_num_mapping[v] -= 1
        cow_num = 0
        for k, v in sec_num_mapping.iteritems():
            if v == 0:
                continue
            guess_val = 0
            if k in guess_num_mapping:
                guess_val = guess_num_mapping[k]
            cow_num += min(guess_val, v)
        return "{0}A{1}B".format(bull_num, cow_num)
