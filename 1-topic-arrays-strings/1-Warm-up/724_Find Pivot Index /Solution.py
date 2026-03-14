class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        sum_l = 0
        sum_r = sum(nums[1:])
        i = 0

        if sum_l == sum_r:
            return i

        while i < len(nums) - 1:

            sum_l += nums[i]
            i += 1
            sum_r -= nums[i]

            if sum_l == sum_r:
                return i

        return -1