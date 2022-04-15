# 给你两个单词word1 和word2， 请返回将word1转换成word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符



class Solution:
    # 暴力破解法
    # def minDistance(self, word1: str, word2: str) -> int:
    #     def dp(i, j):
    #         if i <= -1: return j+1
    #         if j <= -1: return i+1
    #         if word1[i] == word2[j]:
    #             return dp(i-1, j-1)
    #         else:
    #             return min(dp(i-1, j)+1, dp(i, j-1)+1, dp(i-1, j-1)+1)
    #
    #     return dp(len(word1)-1, len(word2)-1)
    # 备忘录法
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dp(i, j):
            if i <= -1: return j+1
            if j <= -1: return i+1
            if (i, j) in memo:
                return memo[(i,j)]
            if word1[i] == word2[j]:
                res = dp(i-1, j-1)
                memo[(i, j)] = res
                return dp(i-1, j-1)
            else:
                memo[(i, j)] = min(dp(i-1, j)+1, dp(i, j-1)+1, dp(i-1, j-1)+1)
                return memo[(i, j)]

        return dp(len(word1)-1, len(word2)-1)

if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    s= Solution()
    res = s.minDistance(word1, word2)
    print(res)