class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # first pass, try to find values that equal k
        dict = {}
        dict[0] = 1
        total = 0

        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in dict:
                total += dict[prefix_sum - k]
                
            if prefix_sum in dict:
                dict[prefix_sum] += 1

            else:
                dict[prefix_sum] = 1
        
        return total

        