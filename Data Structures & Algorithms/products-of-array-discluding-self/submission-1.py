class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = n * [1]
        left = n * [1]
        
        #right array
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        #left array
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
            print(left[i])

        result = [right[i] * left[i] for i in range(len(nums))]
        return result
        
       


        