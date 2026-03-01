class Solution:
    def sortColors(self, nums: List[int]) -> None:

        low, i , high = 0, 0, len(nums)-1
        while i <= high:
            if nums[i] == 0:
                nums[low], nums[i] = nums[i], nums[low]
                i += 1
                low += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[high], nums[i] = nums[i], nums[high]
                high -= 1
        return nums