class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        num_set = set(nums)
        tracker = 1
        max_tracker = 1
        
        for num in num_set:
            if num - 1 not in num_set:
                while num + tracker in num_set:
                    tracker += 1
                    max_tracker = max(max_tracker, tracker)
                tracker = 1
            
        return max(max_tracker, tracker)



        