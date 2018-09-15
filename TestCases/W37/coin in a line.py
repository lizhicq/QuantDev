class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        if len(values) < 3:
            return True
        n = len(values)
        dp = [0 for i in range(n+1)]
        dp[n-1] = values[n-1]
        dp[n-2] = values[n-2] + values[n-1]
        dp[n-3] = values[n-3] + values[n-2]

        for i in range(n-4, -1, -1):
            dp[i] = max(values[i] + min(dp[i+2], dp[i+3]),
                        values[i] + values[i+1] + min(dp[i+3], dp[i+4]))

        return sum(values) - dp[0] < dp[0]
