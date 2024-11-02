class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[-1])
        operators = {"+", "-", "*", "/"}
        stack = []
        for c in tokens:
            if c in operators:
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(eval(f"{val2} {c} {val1}")))
            else:
                stack.append(c)
        return stack[-1]
