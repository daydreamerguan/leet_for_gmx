class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climbStairsWithResult(n, 0, {})
        
    def climbStairsWithResult(self, n, cnt, cnt_result):
        if cnt in cnt_result:
            return cnt_result[n]
        if cnt == n :
            return 1
        final_result = self.climbStairsWithResult(n, cnt + 1, cnt_result)
        if cnt + 2 <= n:
            final_result += self.climbStairsWithResult(n, cnt + 2, cnt_result)
        cnt_result[cnt] = final_result
        return final_result