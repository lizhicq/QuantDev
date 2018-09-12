class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        f = [[matrix[i][j] for j in range(n)]
                           for i in range(m)]
        res = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    f[i][j] = min(f[i-1][j-1], f[i][j-1], f[i-1][j]) + 1
                    res = max(res, f[i][j])

        for _ in f:
            print _

        return res * res


if __name__ == "__main__":
    s = Solution()
    sample = [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]
    print s.maxSquare(sample)