# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
#
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回-1 。
#
# 你可以认为每种硬币的数量是无限的。


from typing import List


class Solution:
    # 暴力递归解法
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     if amount == 0: return 0
    #     if amount < 0: return -1
    #     res = float('inf')
    #     for coin in coins:
    #         print(coin)
    #         sub_total = self.coinChange(coins, amount-coin)
    #         if sub_total == -1:
    #             continue
    #         print(sub_total)
    #         res = min(sub_total+1, res)
    #     return res if res != float('inf') else -1
    # 备忘录法
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     helper = [-666] * (amount+1)
    #     return self.helper(coins, amount, helper)
    #
    #
    # def helper(self, coins: List[int], amount: int, helper):
    #     if amount == 0: return 0
    #     if amount < 0: return -1
    #     if helper[amount] != -666:
    #         return helper[amount]
    #     res = float('inf')
    #     for coin in coins:
    #         # print(coin)
    #         sub_total = self.helper(coins, amount-coin, helper)
    #         if sub_total == -1:
    #             continue
    #         # print(sub_total)
    #         res = min(sub_total+1, res)
    #     helper[amount] = res if res != float('inf') else -1
    #     return helper[amount]
    # 动态规划
    # 状态：目标金额amount
    # 选择：coins
    # 函数定义：凑出amount，需要coinChange个硬币
    # base case dp[0] = 0
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        print(dp)
        for i in range(len(dp)):
            for coin in coins:
                if i-coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coin]+1)

        return -1 if dp[amount] == amount+1 else dp[amount]


if __name__ == '__main__':
    s = Solution()
    res = s.coinChange([1,2, 5], 100)
    print(res)