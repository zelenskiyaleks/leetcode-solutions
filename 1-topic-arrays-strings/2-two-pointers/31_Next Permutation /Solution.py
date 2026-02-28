class Solution:
    def nextPermutation(self, nums):
        l = len(nums)
        i = l - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i-=1
        if i == 0:
            return nums.reverse()
        pivot = i - 1
        i = l - 1
        while nums[i] <= nums[pivot]:
            i -= 1
        nums[pivot], nums[i] = nums[i], nums[pivot]

        left = pivot + 1
        right = l - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums