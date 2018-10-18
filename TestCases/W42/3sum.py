class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums) < 3:
            return []
        if len(nums) == 3 :
            if sum(nums) == 0:
                return [nums]
            return []

        ans = []
        i = 1
        while i < len(nums) - 1:
            self.check(i-1, i+1, nums, ans, nums[i])
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
        return ans

    def check(self, lo, hi, nums, ans, target):
        while lo >= 0 and hi < len(nums):
            if nums[lo] + target + nums[hi] == 0:
                ans.append([nums[lo], target, nums[hi]])
                while lo >= 0 and nums[lo] + target + nums[hi] == 0:
                    lo -= 1
            elif nums[lo] + target + nums[hi] < 0:
                hi += 1
            else:
                lo -= 1


if __name__ == "__main__":
    s = Solution()
    print s.threeSum([-1, 0, 1, 2, -1, -4])