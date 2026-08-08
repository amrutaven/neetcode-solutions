class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0: return 0
        if len(s) == 1: return 1

        seen = set()

        left = 0
        right = 1

        max_length = 0
        current_length = 1

        seen.add(s[left])
        while (right < len(s)):

            if s[right] not in seen:
                seen.add(s[right])
                max_length = max(right - left + 1, max_length) 
                right += 1

            else: 
                seen.remove(s[left])
                left += 1
        
        return max_length
            




            

            




