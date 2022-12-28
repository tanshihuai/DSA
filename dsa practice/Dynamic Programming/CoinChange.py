class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = [99999] * (amount+1)
        memo[0] = 0

        for i in range(1, amount+1):
            for j in coins:
                if i == j:
                    memo[i] = 1
                elif i-j < 0:
                    continue
                memo[i] = min(memo[i], memo[i-j] + 1)

        return memo[amount] if memo[amount] != 99999 else -1


coins = [2147483647]
amount = 2
s = Solution()
print(s.coinChange(coins, amount))