class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_new = ""
        
        for c in s:
            if c.isalpha():
                s_new += c.lower()
            if c.isdigit():
                s_new += c
        
        pal_range = len(s_new) // 2
        for i in range(pal_range):
            if s_new[i] != s_new[len(s_new) - i - 1]:
                return False
        
        return True