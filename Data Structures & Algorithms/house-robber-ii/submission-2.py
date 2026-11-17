class Solution:
    def rob(self, nums: List[int]) -> int:
        #two memos, one for everything except the last
        #another for everything except the first

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        memo_one = (len(nums)) * [0]
        memo_two = (len(nums)) * [0]

        memo_one[0] = nums[0]
        memo_one[1] = max(nums[0], nums[1])

        memo_two[1] = nums[1]
        memo_two[2] = max(nums[1], nums[2])

        #populate memo_one first
        for i in range(2, len(nums) - 1):
            memo_one[i] = max(nums[i] + memo_one[i - 2], memo_one[i - 1])
        
        #memo_two
        for i in range(3, len(nums)):
            memo_two[i] = max(nums[i] + memo_two[i - 2], memo_two[i - 1])
        
        return max(memo_one[-2], memo_two[-1])

        
        