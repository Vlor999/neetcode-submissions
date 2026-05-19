class Solution:
    opening = ["[", "{", "("]
    closing = ["]", "}", ")"]
    def isValid(self, s: str) -> bool:
        stack = []
        for obj in s:
            if obj in self.opening:
                stack.append(obj)
            else:
                i = self.closing.index(obj)
                if not stack or stack.pop() != self.opening[i]:
                    return False
        return not stack
