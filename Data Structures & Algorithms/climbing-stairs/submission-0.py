class Solution:
    def climbStairs(self, n: int) -> int:
        u, v = 1 , 1
        for i in range(n-1):
            temp  = u
            u = u + v
            v = temp

        return u