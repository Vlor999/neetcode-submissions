class Solution:
    ops = "+-*/"
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok not in self.ops:
                stack.append(tok)
            else:
                op = tok
                right = int(stack.pop())
                left = int(stack.pop())
                if op == "+":
                    val = right + left
                elif op == "-":
                    val = left - right
                elif op == "*":
                    val = left * right
                else:
                    val = int(left / right)
                stack.append(str(val))
            print(stack)
        return int(stack[0])
        

            
        