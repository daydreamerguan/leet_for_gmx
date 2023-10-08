class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ret_value_stack = []
        self.evalRPNWithStack(tokens, 0, ret_value_stack)
        return ret_value_stack[0]

    def evalRPNWithStack(self, tokens, idx, value_stack):
        import math
        if idx >= len(tokens):
            return
        cnt_token = tokens[idx]
        token_without_negtive = cnt_token
        if token_without_negtive.startswith("-"):
            token_without_negtive = token_without_negtive[1:]
        if token_without_negtive.isdigit():
            value_stack.append(int(cnt_token))
            self.evalRPNWithStack(tokens, idx + 1, value_stack)
        else:
            operator_right = value_stack.pop()
            operator_left = value_stack.pop()
            result = 0
            if cnt_token == "-":
                result = operator_left - operator_right
            elif cnt_token == "+":
                result = operator_left + operator_right
            elif cnt_token == "*":
                result = operator_left * operator_right
            else:
                result = operator_left * 1.0 / operator_right
            result = math.trunc(result)
            value_stack.append(result)token
            self.evalRPNWithStack(tokens, idx + 1, value_stack)

if __name__ == '__main__':
    Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])


        
