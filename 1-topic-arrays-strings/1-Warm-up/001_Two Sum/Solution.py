class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict_diff = {}
        for i in range(len(nums)):
            if target - nums[i] in dict_diff:
                return [i, dict_diff[target - nums[i]]]
            dict_diff[nums[i]] = i
            
        return []