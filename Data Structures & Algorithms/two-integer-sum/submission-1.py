class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for num in range(len(nums)):
            if target - nums[num] not in num_dict:
                num_dict[nums[num]] = num
            else:
                return [num_dict[target - nums[num]], num]

            
        