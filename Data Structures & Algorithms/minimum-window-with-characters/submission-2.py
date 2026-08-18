class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        
        if t == s: return s

        t_book = {}

        for c in t:
            if c not in t_book:
                t_book[c] = 1
            else:
                t_book[c] += 1
        
        right = 0
        left = 0
        min_string = None
        cur_string = ""
        t_copy = t_book.copy()

        while (right < len(s)):
            if s[right] in t_copy:
                t_copy[s[right]] -= 1
                right += 1

            else:
                right += 1
            
            #keep shrinking here
            while all(value <= 0 for value in t_copy.values()):
                cur_string = s[left:right]

                if min_string is None or len(min_string) > len(cur_string):
                    min_string = cur_string

                if s[left] in t:
                    t_copy[s[left]] += 1
                left += 1
        
        if min_string is None:
            return ""
        
        return min_string


            

                
        
        