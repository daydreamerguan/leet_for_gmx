class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        final_list = []
        # it is a stack , * is the pop function
        for character in s:
        	if character != "*":
        		final_list.append(character)
        	else:
        		if len(final_list) > 0: 
        			final_list.pop()
        return "".join(final_list)