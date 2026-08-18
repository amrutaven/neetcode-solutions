class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        
        book = {}
        right = 0
        left = 0
        final_max = 0


        while right < len(s):
            if s[right] not in book:
                book[s[right]] = 1
            else:
                book[s[right]] += 1
            
            right += 1
            window_rn = right - left
            book_max = max(book.values())

            if window_rn - book_max <= k:
                final_max = max(final_max, window_rn)
            else:
                book[s[left]] -= 1
                left += 1
            
        return final_max
            


        