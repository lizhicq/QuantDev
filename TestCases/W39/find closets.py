class Solution(object):
    def get_closest(self, A, target, k):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        if A[end] - target < target - A[start]:
            mid = end
        else:
            mid = start

        ans = []

        while len(ans) < k:
            left_dif = target - A[start] if start >= 0 else None
            right_dif = A[end] - target if end < len(A) else None



