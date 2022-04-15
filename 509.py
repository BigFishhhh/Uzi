# 斐波那契数（通常用F(n) 表示）形成的序列称为 斐波那契数列 。该数列由0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
#
# F(0) = 0，F(1)= 1
# F(n) = F(n - 1) + F(n - 2)，其中 n > 1
# 给定n ，请计算 F(n) 。

class Solution:

    # 递归算法
    # def fib(self, n: int) -> int:
    #     if (n == 0 or n==1):
    #         return n
    #     return self.fib(n-1) + self.fib(n-2)
    # 备忘录算法
    # def fib(self, n: int) -> int:
    #     help_dict = {1:1, 2:2}
    #     return self.helper(n, help_dict)
    #
    # def helper(self, n, help_dict):
    #     if n == 0 or n == 1:
    #         return n
    #     if n in help_dict:
    #         return help_dict[n]
    #     help_dict[n] = self.helper(n-1, help_dict) + self.helper(n-2, help_dict)
    #     return help_dict[n]

    # 动态规划算法1
    # def fib(self, n: int) -> int:
    #     if n == 0 or n == 1:
    #         return n
    #     dp = [0] * (n+1)
    #     dp[0], dp[1] = 0, 1
    #     for i in range(2, n+1):
    #         dp[i] = dp[i-1] + dp[i-2]
    #     return dp[n]

    # 动态规划算法2
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        prev, curr = 0, 1
        for i in range(2, n + 1):
            total = prev + curr
            prev = curr
            curr = total
        return curr



if __name__ == '__main__':
    s = Solution()
    s.fib(10)