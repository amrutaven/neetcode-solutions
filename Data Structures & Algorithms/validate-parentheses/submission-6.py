class Solution:
    def isValid(self, s: str) -> bool:
        map = {}
        map['('] = ')'
        map['{'] = '}'
        map['['] = ']'

        stack = []

        for c in s:
            if c in map:
                stack.append(c)
            else:
                if not stack or c != map[stack[-1]]:
                    return False
                stack.pop()
        
        return not stack


        