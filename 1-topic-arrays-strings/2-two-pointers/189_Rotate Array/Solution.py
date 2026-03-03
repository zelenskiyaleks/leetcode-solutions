class SolutionReverse:
    """
    Approach 1 — In-place reversal
    """

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        self._reverse(nums, 0, n - 1)
        self._reverse(nums, 0, k - 1)
        self._reverse(nums, k, n - 1)

    def _reverse(self, nums: List[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


class SolutionSlicing:
    """
    Approach 2 — Python slicing
    """

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[:] = nums[n - k:] + nums[:n - k]