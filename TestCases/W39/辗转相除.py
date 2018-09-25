class Solution(object):
    def gcd(self, big, small):
        if big < small:
            big, small = small, big
        if small == 0:
            return big
        else:
            return self.gcd(small, big % small)


if __name__ == "__main__":
    s = Solution()
    print s.gcd(72, 64)