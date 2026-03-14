class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = 1
        candidate = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == candidate:
                k += 1
            else:
                k -= 1
                if k < 0:
                    candidate = nums[i]
                    k = 1
        return candidate