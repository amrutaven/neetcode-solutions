class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}
        for c, u in zip(s, t):
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1
            
            if u in t_dict:
                t_dict[u] += 1
            else:
                t_dict[u] = 1
        
        return s_dict == t_dict

        