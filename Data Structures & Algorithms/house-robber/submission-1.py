class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
            

        memo = len(nums) * [0]
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])

        for i in range(1, len(nums)):
            memo[i] = max(nums[i] + memo[i - 2], memo[i - 1])
        
        return memo[len(nums) - 1]


        


        