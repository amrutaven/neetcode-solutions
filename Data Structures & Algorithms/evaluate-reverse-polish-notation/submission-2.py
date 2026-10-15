class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            if val not in ['+', '-', '*', '/']:
                stack.append(val)
            else:
                num_two = int(stack[-1])
                stack.pop()
                num_one = int(stack[-1])
                stack.pop()

                if val == '+':
                    stack.append(num_one + num_two)
                if val == '-':
                    stack.append(num_one - num_two)
                if val == '*':
                    stack.append(num_two * num_one)
                if val == '/':
                    stack.append(num_one / num_two)
        
        return int(stack[-1])




        