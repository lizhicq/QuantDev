class Solution:
    """
    @param: A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        m, n = len(A), len(A[0])
        return self.find(1, m-2, 1, n-2, A)


    def find(self, x1, x2, y1, y2, A):
        mid1 = (x1 + x2) / 2
        mid2 = (y1 + y2) / 2

        x, y = mid1, mid2
        max_ = A[mid1][mid2]

        for j in range(y1, y2+1):
            if A[mid1][j] > max_:
                max_ = A[mid1][j]
                x = mid1
                y = j

        for i in range(x1, x2+1):
            if A[i][mid2] > max_:
                max_ = A[i][mid2]
                x = i
                y = mid2

        if A[x-1][y] > A[x][y]:
            x -= 1
        elif A[x+1][y] > A[x][y]:
            x += 1
        elif A[x][y-1] > A[x][y]:
            y -= 1
        elif A[x][y+1] > A[x][y]:
            y += 1
        else:# peak
            return [x,y]

        if x1 <= x < mid1 and y1 <= y < mid2:
            return self.find(x1, mid1-1, y1, mid2-1, A)
        if x1 <= x < mid1 and mid2 < y <= y2:
            return self.find(x1, mid1-1, mid2+1, y2, A)
        if mid1 < x <= x2 and y1 < y < mid2:
            return self.find(mid1+1, x2, y1, mid2-1, A)
        if mid1 < x <= x2 and mid2 < y <= y2:
            return self.find(mid1+1, x2, mid2+1, y2, A)

        return [-1,-1]

if __name__ == "__main__":
    s = Solution()
    print(s.findPeakII([[1,2,1,2,1,2,1],
                        [2,17,13,6,5,17,2],
                        [1,15,8,10,8,15,1],
                        [2,14,12,11,12,14,2],
                        [1,2,1,2,1,2,1]]))